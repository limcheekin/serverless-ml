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
COPY download_flan-t5-xxl.sh .
RUN chmod +x download_flan-t5-xxl.sh && \
    ./download_flan-t5-xxl.sh && \
    rm download_flan-t5-xxl.sh

# Convert model
RUN ct2-transformers-converter --model google/flan-t5-xxl --output_dir google/flan-t5-xxl-ct2 --copy_files tokenizer.json tokenizer_config.json special_tokens_map.json spiece.model --quantization int8 --force --low_cpu_mem_usage && \
    rm -rf google/flan-t5-xxl

COPY README.md google/flan-t5-xxl-ct2/

ARG HF_TOKEN
ENV HF_TOKEN=$HF_TOKEN
COPY hf_upload_model.py ./
RUN python hf_upload_model.py

# Runtime Stage
FROM public.ecr.aws/lambda/python:3.10

# Copy built files from the build stage
RUN mkdir google
COPY --from=build ./google ./google

RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir transformers ctranslate2 sentencepiece && \
    pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip uninstall -y pip setuptools wheel

COPY app.py ./
CMD ["app.handler"]
