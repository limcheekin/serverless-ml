# REF: https://aws.amazon.com/blogs/machine-learning/using-container-images-to-run-pytorch-models-in-aws-lambda/
# Build Stage
FROM python:3.10-slim as build

# Install build dependencies
RUN apt-get update && \
    apt-get install -y curl

RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir transformers ctranslate2 sentencepiece accelerate && \
    pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip uninstall -y pip wheel

# Download and prepare model
COPY download_flan-t5-xl.sh .
RUN chmod +x download_flan-t5-xl.sh && \
    ./download_flan-t5-xl.sh && \
    rm download_flan-t5-xl.sh

# Convert model and cleanup unnecessary files
RUN ct2-transformers-converter --model google/flan-t5-xl --output_dir google/flan-t5-xl-ct2 --quantization int8 --low_cpu_mem_usage && \
    rm -rf google/flan-t5-xl/*.bin

# Runtime Stage
FROM public.ecr.aws/lambda/python:3.10

# Copy built files from the build stage
RUN mkdir google
COPY --from=build ./google ./google

RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir transformers ctranslate2 sentencepiece accelerate && \
    pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip uninstall -y pip setuptools wheel

COPY app.py ./
CMD ["app.handler"]
