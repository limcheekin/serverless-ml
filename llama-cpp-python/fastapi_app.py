# Modal Lab web app for llama.cpp.
from modal import Image, Stub, asgi_app

stub = Stub("llama-cpp-python")

image = Image.from_dockerfile(
                "Dockerfile", force_build=True
            ).pip_install("pydantic_settings").pip_install("fastapi").env(
                {"MODEL": "/model/ggml-model-q8_0.bin"}
            )


@stub.function(image=image, cpu=14, memory=20480, keep_warm=1, timeout=1800)
@asgi_app()
def fastapi_app():
    from llama_cpp.server.app import create_app, Settings
    import os
    print("os.cpu_count()", os.cpu_count())
    return create_app(Settings(n_threads=os.cpu_count()))


if __name__ == "__main__":
    stub.deploy("webapp")
