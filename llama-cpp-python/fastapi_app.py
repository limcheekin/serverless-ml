# Modal Lab web app for llama.cpp.
from modal import Image, Stub, asgi_app
import os

stub = Stub("llama-cpp-python")


def download_model():
    from huggingface_hub import hf_hub_download
    hf_hub_download(repo_id="vihangd/open_llama_7b_300bt_ggml",
                    filename="ggml-model-q4_0.bin",
                    local_dir="model",
                    token=os.environ["HF_TOKEN"])


image = Image.debian_slim().env({
    "MODEL": "./model/ggml-model-q4_0.bin",
    "HF_TOKEN": os.environ["HF_TOKEN"],
    "CMAKE_ARGS": "-DLLAMA_OPENBLAS=on",
    "FORCE_CMAKE": 1
}).pip_install("llama-cpp-python[server]", "huggingface-hub").run_function(download_model)


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    from llama_cpp.server.app import create_app
    return create_app()


if __name__ == "__main__":
    stub.deploy("webapp")
