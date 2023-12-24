# Grab a fresh copy of the Python image
FROM python:3.11-slim

# Install build and runtime dependencies
RUN apt-get update && \
    apt-get install -y \
    libopenblas-dev \
    ninja-build \
    build-essential \
    pkg-config \
    curl

RUN pip install -U pip setuptools wheel && \
    CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" FORCE_CMAKE=1 pip install --no-cache-dir llama-cpp-python[server]

# Download model
RUN mkdir model && \
    curl -L https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q6_K.gguf -o model/gguf-model.bin
