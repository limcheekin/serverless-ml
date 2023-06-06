from typing import Optional

from fastapi import FastAPI, Header
from pydantic import BaseModel

from modal import Image, Stub, asgi_app, Mount
import os

model_name = os.environ["MODEL"]
index = model_name.rindex("/") + 1
stub_name = model_name[index:]
web_app = FastAPI()
stub = Stub(stub_name)
image = Image.from_dockerfile("Dockerfile", context_mount=Mount.from_local_dir(
    ".", remote_path="."), force_build=True).env({"MODEL": model_name})
stub.image = image

if stub.is_inside(stub.image):
    from transformers import AutoTokenizer
    import ctranslate2
    import os
    print(f"loading {os.environ['MODEL']} model...")
    generator = ctranslate2.Generator(os.environ["MODEL"]))
    tokenizer = AutoTokenizer.from_pretrained(os.environ["MODEL"])
    print('model loaded\n')


class Response(BaseModel):
    prompt: str


class Request(BaseModel):
    prompt: str
    params: Optional[dict] = {}


@web_app.get("/")
async def handle_root(user_agent: Optional[str] = Header(None)):
    print(f"GET /     - received user_agent={user_agent}")
    return "Hello World"


@web_app.post("/")
async def handle(request: Request, user_agent: Optional[str] = Header(None)):
    print(
        f"POST / - received user_agent={user_agent}, request.prompt={request.prompt}, request.params={request.params}"
    )

    input_tokens = tokenizer.convert_ids_to_tokens(
        tokenizer.encode(request.prompt))
    results = generator.generate_batch([input_tokens], **request.params)
    output_tokens = results[0].sequences_ids[0]
    result = tokenizer.decode(output_tokens)
    print(f"result: {result}")
    return Response(prompt=result)


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    return web_app


if __name__ == "__main__":
    stub.deploy("webapp")
