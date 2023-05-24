# REF: https://aws.amazon.com/blogs/machine-learning/using-container-images-to-run-pytorch-models-in-aws-lambda/
# Build Stage
FROM python:3.10-slim as build

# Install build dependencies
RUN apt-get update && \
    apt-get install -y curl

RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir transformers ctranslate2 sentencepiece accelerate && \
    pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip uninstall -y pip setuptools wheel

# Download and prepare model
COPY download_fastchat-t5-3b.sh .
RUN chmod +x download_fastchat-t5-3b.sh && \
    ./download_fastchat-t5-3b.sh && \
    rm download_fastchat-t5-3b.sh

# Convert model and cleanup unnecessary files
RUN ct2-transformers-converter --model lmsys/fastchat-t5-3b --output_dir lmsys/fastchat-t5-3b-ct2 --quantization int8 --low_cpu_mem_usage && \
    rm -rf lmsys/fastchat-t5-3b/pytorch_model.bin

# Runtime Stage
FROM public.ecr.aws/lambda/python:3.10

# Copy built files from the build stage
RUN mkdir lmsys
COPY --from=build ./lmsys ./lmsys

RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir transformers ctranslate2 sentencepiece && \
    pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip uninstall -y pip setuptools wheel

COPY app.py ./
CMD ["app.handler"]
