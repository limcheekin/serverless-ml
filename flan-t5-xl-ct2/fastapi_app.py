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
    ".", remote_path=".")).env({"MODEL": model_name})
stub.image = image

if stub.is_inside(stub.image):
    from transformers import AutoTokenizer
    import ctranslate2
    import os
    print(f"loading {os.environ['MODEL']} model...")
    translator = ctranslate2.Translator(os.environ["MODEL"])
    tokenizer = AutoTokenizer.from_pretrained(os.environ["MODEL"])
    print('model loaded\n')


class Response(BaseModel):
    prompt: str


class Request(BaseModel):
    prompt: str
    params: Optional[dict] = {
        "beam_size": 2,
        "top_k": 1,              # sampling_topk
        "temperature": 1.0,      # sampling_temperature
        "repeat_penalty": 1.0,   # repetition_penalty
        "no_repeat_ngram_size": 0,
        "min_length": 1,         # min_decoding_length
        "max_length": 256,       # max_decoding_length
    }


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
    results = translator.translate_batch(
        [input_tokens],
        beam_size=request.params["beam_size"],
        sampling_topk=request.params["top_k"],
        sampling_temperature=request.params["temperature"],
        repetition_penalty=request.params["repeat_penalty"],
        no_repeat_ngram_size=request.params["no_repeat_ngram_size"],
        min_decoding_length=request.params["min_length"],
        max_decoding_length=request.params["max_length"],
    )
    output_tokens = results[0].hypotheses[0]
    result = tokenizer.decode(
        tokenizer.convert_tokens_to_ids(output_tokens))
    print(f"result: {result}")
    return Response(prompt=result)


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    return web_app


if __name__ == "__main__":
    stub.deploy("webapp")
