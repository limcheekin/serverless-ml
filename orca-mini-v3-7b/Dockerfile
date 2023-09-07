# Grab a fresh copy of the Python image
FROM python:3.10-slim

# Install build and runtime dependencies
RUN apt-get update && \
    apt-get install -y \
    libopenblas-dev \
    ninja-build \
    build-essential \
    pkg-config \
    curl

RUN pip install -U pip setuptools wheel && \
    CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" FORCE_CMAKE=1 pip install llama-cpp-python[server]

# Download model
RUN mkdir model && \
    curl -L https://huggingface.co/TheBloke/orca_mini_v3_7B-GGML/resolve/main/orca_mini_v3_7b.ggmlv3.q4_0.bin -o model/ggml-model.bin
