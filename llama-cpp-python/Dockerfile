# REF: https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/
# The download size of `python:3.10-slim-bullseye` is **45MB**¹. Its uncompressed on-disk size is **125MB**¹.
# (1) The best Docker base image for your Python application (March 2023). https://pythonspeed.com/articles/base-image-python-docker-images/.
# (2) Reduce the size of container images with DockerSlim. https://developers.redhat.com/articles/2022/01/17/reduce-size-container-images-dockerslim.

# Grab a fresh copy of the Python image
FROM python:3.11-slim

# Install build and runtime dependencies
RUN apt-get update && \
    apt-get install -y \
    libopenblas-dev \
    ninja-build \
    build-essential \
    wget

RUN pip install -U pip setuptools wheel && \
    CMAKE_ARGS="-DLLAMA_OPENBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python[server]

# Download model
RUN mkdir model && \
    curl -L https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q8_0.bin -o model/ggml-model-q8_0.bin