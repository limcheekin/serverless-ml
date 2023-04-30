# REF: https://aws.amazon.com/blogs/machine-learning/using-container-images-to-run-pytorch-models-in-aws-lambda/
# REF: https://heidloff.net/article/running-llm-flan-t5-locally/
FROM public.ecr.aws/lambda/provided:al2.2023.04.17.19

COPY app.py ./

# Install dependencies
# REF: https://github.com/atilaromero/gpt4all-j-in-docker/blob/master/Dockerfile
RUN apt update
RUN apt-get install -y \
    libglib2.0-0 \
    libbrotli1 \
    libdrm2 \
    libgbm1 \
    libjpeg-turbo8 \
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

RUN pip install -U pip setuptools wheel
RUN pip install awslambdaric
RUN pip install gpt4all-j

# download the model file
RUN mkdir model
RUN curl -L https://gpt4all.io/models/ggml-gpt4all-j.bin -o ./model/ggml-gpt4all-j

CMD ["app.handler"]
