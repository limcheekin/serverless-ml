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
    curl -L https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v0.6/resolve/main/ggml-model-q4_0.gguf -o model/gguf-model.bin
