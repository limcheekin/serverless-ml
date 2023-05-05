# REF: https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/
# The download size of `python:3.10-slim-bullseye` is **45MB**¹. Its uncompressed on-disk size is **125MB**¹.
# (1) The best Docker base image for your Python application (March 2023). https://pythonspeed.com/articles/base-image-python-docker-images/.
# (2) Reduce the size of container images with DockerSlim. https://developers.redhat.com/articles/2022/01/17/reduce-size-container-images-dockerslim.
# Define global args
ARG FUNCTION_DIR="/home/app/"
ARG RUNTIME_VERSION="3.10"

# Stage 1 - bundle base image + runtime
# Grab a fresh copy of the image and install GCC
FROM python:${RUNTIME_VERSION}-slim-bullseye AS python-slim-bullseye

# Stage 2 - build function and dependencies
FROM python-slim-bullseye AS build-image
# Install aws-lambda-cpp build dependencies
# REF: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html
RUN apt-get update && \
    apt-get install -y \
    libopenblas-dev \
    ninja-build \
    build-essential \
    curl

# Include global args in this stage of the build
ARG FUNCTION_DIR
ARG RUNTIME_VERSION
# Create function directory
RUN mkdir -p ${FUNCTION_DIR}
# Copy handler function
COPY app.py ${FUNCTION_DIR}
# Optional – Install the function's dependencies
COPY requirements.txt ./
RUN python${RUNTIME_VERSION} -m pip install -r requirements.txt --target ${FUNCTION_DIR}
# Install Lambda Runtime Interface Client for Python
RUN python${RUNTIME_VERSION} -m pip install awslambdaric --target ${FUNCTION_DIR}

# download the model file
RUN mkdir ${FUNCTION_DIR}/model
RUN curl -L https://huggingface.co/vihangd/open_llama_7b_300bt_ggml/resolve/main/ggml-model-q8_0.bin -o ./model/openllama-7b-300bt-ggml-q8_0.bin

# Stage 3 - final runtime image
# Grab a fresh copy of the Python image
FROM python-slim-bullseye

# Install runtime dependencies
#RUN apt-get update && \
#    apt-get install -y \
#    libglib2.0-0 \
#    libbrotli1 \

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}
# Copy in the built dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}
# (Optional) Add Lambda Runtime Interface Emulator and use a script in the ENTRYPOINT for simpler local runs
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
COPY entry.sh /
RUN chmod 755 /usr/bin/aws-lambda-rie /entry.sh
ENTRYPOINT [ "/entry.sh" ]
CMD [ "app.handler" ]
