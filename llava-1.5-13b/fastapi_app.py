# Modal Lab web app for llama.cpp.
from modal import Image, Stub, asgi_app

stub = Stub("llava-1.5-13b")

image = Image.from_dockerfile(
    "Dockerfile", force_build=True
).pip_install("pydantic_settings").pip_install("fastapi==0.103.1").run_commands(
    # Fix: Cannot allocate memory. Try increasing RLIMIT_MLOCK ('ulimit -l' as root).
    'echo "* soft memlock unlimited" >> /etc/security/limits.conf && echo "* hard memlock unlimited" >> /etc/security/limits.conf',
)


@stub.function(image=image, cpu=14, memory=12288, keep_warm=1, timeout=600)
@asgi_app()
def fastapi_app():
    from llama_cpp.server.app import create_app, Settings
    import os
    print("os.cpu_count()", os.cpu_count())
    app = create_app(
        Settings(
            n_threads=14,
            model="/model/gguf-model.bin",
            embedding=False
        )
    )
    return app


if __name__ == "__main__":
    stub.deploy("webapp")
