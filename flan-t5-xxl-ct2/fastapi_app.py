from typing import Optional

from fastapi import FastAPI, Header
from pydantic import BaseModel

from modal import Image, Stub, asgi_app, web_endpoint

from transformers import AutoTokenizer
import ctranslate2

web_app = FastAPI()
stub = Stub("flan-t5-xxl-ct2")
translator = None
tokenizer = None

# image = Image.debian_slim()
image = Image.from_dockerfile("Dockerfile")


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
        f"POST /foo - received user_agent={user_agent}, item.name={item.name}"
    )
    return item


def load_model():
    print('loading model...')
    translator = ctranslate2.Translator("google/flan-t5-xxl-ct2")
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-xxl-ct2")
    print('model loaded\n')


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    load_model()
    return web_app


if __name__ == "__main__":
    stub.deploy("webapp")
