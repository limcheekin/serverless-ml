from typing import Optional

from fastapi import FastAPI, Header
from pydantic import BaseModel

from modal import Image, Stub, asgi_app, Mount

web_app = FastAPI()
stub = Stub("mpt-7b-storywriter-ct2")
image = Image.from_dockerfile("Dockerfile", context_mount=Mount.from_local_dir(
    ".", remote_path="."))
stub.image = image

if stub.is_inside(stub.image):
    from transformers import AutoTokenizer
    import ctranslate2
    print('loading model...')
    generator = ctranslate2.Generator("/mosaicml/mpt-7b-storywriter-ct2")
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
    print('model loaded.')


class Response(BaseModel):
    completion: str


class Request(BaseModel):
    prompt: str
    params: Optional[dict] = None


@web_app.get("/")
async def handle_root(user_agent: Optional[str] = Header(None)):
    print(f"GET /     - received user_agent={user_agent}")
    return "Hello World"


@web_app.post("/")
async def handle(request: Request, user_agent: Optional[str] = Header(None)):
    print(
        f"POST / - received user_agent={user_agent}, request.prompt={request.prompt}"
    )
    input_tokens = tokenizer.convert_ids_to_tokens(
        tokenizer.encode(request.prompt))
    results = generator.generate_batch(
        [input_tokens], max_length=256, sampling_topk=10)
    text = tokenizer.decode(results[0].sequences_ids[0])
    print(f"text: {text}")
    return Response(completion=text)


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    return web_app


if __name__ == "__main__":
    stub.deploy("webapp")
