# Modal Lab web app for llama.cpp.
from modal import Image, Stub, asgi_app

stub = Stub("orca-mini-v3-7b")

image = Image.from_dockerfile(
    "Dockerfile", force_build=True
).pip_install("pydantic_settings").pip_install("fastapi==0.100.1")


@stub.function(image=image, cpu=14, memory=5120, keep_warm=1, timeout=600)
@asgi_app()
def fastapi_app():
    from llama_cpp.server.app import create_app, Settings
    import os
    print("os.cpu_count()", os.cpu_count())
    app = create_app(
        Settings(
            n_threads=14,
            model="/model/ggml-model.bin",
            embedding=False
        )
    )
    return app


if __name__ == "__main__":
    stub.deploy("webapp")
