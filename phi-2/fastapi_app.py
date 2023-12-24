# Modal Lab web app for llama.cpp.
from modal import Image, Stub, asgi_app

stub = Stub("phi-2")

image = Image.from_dockerfile(
    "Dockerfile", force_build=True
).pip_install("pydantic_settings").pip_install("fastapi==0.105.0").run_commands(
    # Fix: Cannot allocate memory. Try increasing RLIMIT_MLOCK ('ulimit -l' as root).
    'echo "* soft memlock unlimited" >> /etc/security/limits.conf && echo "* hard memlock unlimited" >> /etc/security/limits.conf',
)


@stub.function(image=image, cpu=4, memory=5632, timeout=600)
@asgi_app()
def fastapi_app():
    from llama_cpp.server.app import create_app, Settings
    import os
    print("os.cpu_count()", os.cpu_count())
    app = create_app(
        Settings(
            n_threads=4,
            model="/model/gguf-model.bin",
            embedding=False,
            chat_format=None
        )
    )
    return app


if __name__ == "__main__":
    stub.deploy("webapp")
