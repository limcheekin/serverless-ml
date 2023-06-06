FROM python:3.10-slim

# Install build dependencies
RUN apt-get update && \
    apt-get install -y git-lfs

RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir transformers ctranslate2 accelerate einops && \
    pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu


# Download and prepare model
COPY download_model.sh .
RUN chmod +x download_model.sh && \
    ./download_model.sh && \
    rm download_model.sh

# Convert model
RUN ct2-transformers-converter --model tiiuae/falcon-7b-instruct --output_dir tiiuae/falcon-7b-instruct-ct2 --copy_files tokenizer.json tokenizer_config.json special_tokens_map.json generation_config.json --quantization int8 --force --low_cpu_mem_usage --trust_remote_code && \
    rm -rf tiiuae/falcon-7b-instruct

COPY README.md tiiuae/falcon-7b-instruct-ct2/

COPY token.txt ./
COPY hf_upload_model.py ./
RUN python hf_upload_model.py