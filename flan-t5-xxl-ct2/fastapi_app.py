from typing import Optional

from fastapi import FastAPI, Header
from pydantic import BaseModel

from modal import Image, Stub, asgi_app, Mount

from transformers import AutoTokenizer
import ctranslate2
import os

web_app = FastAPI()
stub = Stub("flan-t5-xxl-ct2")
translator = None
tokenizer = None


image = Image.from_dockerfile("Dockerfile", context_mount=Mount.from_local_dir(
    ".", remote_path="."))


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
    results = translator.translate_batch([input_tokens])
    output_tokens = results[0].hypotheses[0]
    result = tokenizer.decode(
        tokenizer.convert_tokens_to_ids(output_tokens))
    print(f"result: {result}")
    return Response(completion=result)


@web_app.on_event('startup')
def init():
    print('loading model...')
    translator = ctranslate2.Translator("/google/flan-t5-xxl-ct2")
    tokenizer = AutoTokenizer.from_pretrained("/google/flan-t5-xxl-ct2")
    print('model loaded\n')


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    return web_app


if __name__ == "__main__":
    stub.deploy("webapp")
