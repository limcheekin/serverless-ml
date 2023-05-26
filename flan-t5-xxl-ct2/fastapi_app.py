from typing import Optional

from fastapi import FastAPI, Header
from pydantic import BaseModel

from modal import Image, Stub, asgi_app, Mount, Secret

from transformers import AutoTokenizer
import ctranslate2
from huggingface_hub import HfApi, create_repo
import os

web_app = FastAPI()
stub = Stub("flan-t5-xxl-ct2")
translator = None
tokenizer = None

# image = Image.debian_slim()
image = Image.from_dockerfile(
    "Dockerfile", context_mount=Mount.from_local_dir(".", remote_path="."))


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


def load_model():
    print('loading model...')
    translator = ctranslate2.Translator("google/flan-t5-xxl-ct2")
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-xxl-ct2")
    print('model loaded\n')


def upload_model():
    create_repo("limcheekin/flan-t5-xxl-ct2",
                token=os.environ["HF_TOKEN"],
                repo_type="model",
                exist_ok=True)
    api = HfApi(token=os.environ["HF_TOKEN"])
    api.upload_folder(
        folder_path="google/flan-t5-xxl-ct2",
        repo_id="limcheekin/flan-t5-xxl-ct2",
    )


@stub.function(image=image, secret=Secret.from_name("upload-model"))
@asgi_app()
def fastapi_app():
    upload_model()
    load_model()
    return web_app


if __name__ == "__main__":
    stub.deploy("webapp")
