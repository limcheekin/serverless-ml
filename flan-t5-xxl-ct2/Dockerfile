FROM python:3.10-slim

# Install build dependencies
RUN apt-get update && \
    apt-get install -y curl

RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir transformers ctranslate2 sentencepiece accelerate && \
    pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu

# Download and prepare model
COPY download_flan-t5-xxl.sh .
RUN chmod +x download_flan-t5-xxl.sh && \
    ./download_flan-t5-xxl.sh && \
    rm download_flan-t5-xxl.sh

# Convert model
RUN ct2-transformers-converter --model google/flan-t5-xxl --output_dir google/flan-t5-xxl-ct2 --copy_files tokenizer.json tokenizer_config.json special_tokens_map.json spiece.model --quantization int8 --force --low_cpu_mem_usage && \
    rm -rf google/flan-t5-xxl

COPY README.md google/flan-t5-xxl-ct2/

COPY hf_upload_model.py ./
RUN python hf_upload_model.py