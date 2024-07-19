from modal import Image, App, asgi_app
import os

app = App(os.environ["APP_NAME"])

image = Image.from_registry("python:3.11-slim-bookworm"
        ).copy_local_file(f"{os.environ['APP_NAME']}.guff"
        ).dockerfile_commands(
            "RUN apt-get update && apt-get install -y libopenblas-dev ninja-build build-essential pkg-config",
            'RUN CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" FORCE_CMAKE=1 pip install --no-cache-dir llama-cpp-python[server]'
        ).env({
            "APP_NAME": os.environ["APP_NAME"],
        })


cpu = float(os.getenv("CPU", 2.0))
memory = int(os.getenv("MEMORY", 2048)) 
timeout = int(os.getenv("TIMEOUT", 600))
keep_warm = int(os.getenv("KEEP_WARM", 1))
@app.function(image=image, cpu=cpu, memory=memory, timeout=timeout, keep_warm=keep_warm)
@asgi_app()
def fastapi_app():
    from llama_cpp.server.app import create_app, Settings
    import os
    print("os.cpu_count()", os.cpu_count())
    return create_app(
        Settings(
            n_threads=os.cpu_count(),
            model=f"/{os.environ['APP_NAME']}.guff"
        )
    )


if __name__ == "__main__":
    app.deploy("webapp")
