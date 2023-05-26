# Modal Lab web app for llama.cpp.
from modal import Image, Stub, asgi_app
from llama_cpp.server.app import create_app

stub = Stub("llama-cpp-python")

image = Image.from_dockerfile("Dockerfile")


@stub.function(image=image)
@asgi_app()
def fastapi_app():
    return create_app()


if __name__ == "__main__":
    stub.deploy("webapp")
