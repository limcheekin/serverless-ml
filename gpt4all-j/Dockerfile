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
# Install GCC (Alpine uses musl but we compile and link dependencies with GCC)
#RUN apk add --no-cache \
#    libstdc++

# Stage 2 - build function and dependencies
FROM python-slim-bullseye AS build-image
# Install aws-lambda-cpp build dependencies
# REF: https://docs.aws.amazon.com/lambda/latest/dg/images-create.html
RUN apt-get update
RUN apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev \
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
RUN curl -L https://gpt4all.io/models/ggml-gpt4all-j.bin -o ${FUNCTION_DIR}/model/ggml-gpt4all-j

# Stage 3 - final runtime image
# Grab a fresh copy of the Python image
FROM python-slim-bullseye

# Install gpt4all-j runtime dependencies
# REF: https://github.com/atilaromero/gpt4all-j-in-docker/blob/master/Dockerfile
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libbrotli1 \
    libdrm2 \
    libgbm1 \
    libjpeg62-turbo \
    libxcb-glx0 \
    libdbus-1-3 \
    libegl1 \
    libpcre2-16-0 \
    libglx0 \
    libopengl0 \
    libpng16-16 \
    libharfbuzz0b \
    libfontconfig1 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    libxcb-cursor0 \
    libxcb-icccm4 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-shape0 \
    libsm6

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
