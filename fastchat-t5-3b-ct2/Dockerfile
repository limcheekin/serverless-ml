FROM python:3.10-slim

# Install build dependencies
RUN apt-get update && \
    apt-get install -y git-lfs

RUN pip install -U pip setuptools wheel && \
    pip install --no-cache-dir transformers ctranslate2 sentencepiece accelerate && \
    pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu


# Download and prepare model
COPY download_model.sh .
RUN chmod +x download_model.sh && \
    ./download_model.sh && \
    rm download_model.sh

# Convert model
RUN ct2-transformers-converter --model lmsys/fastchat-t5-3b --output_dir lmsys/fastchat-t5-3b-ct2 --copy_files added_tokens.json tokenizer_config.json special_tokens_map.json spiece.model --quantization int8 --force --low_cpu_mem_usage && \
    rm -rf lmsys/fastchat-t5-3b

COPY README.md lmsys/fastchat-t5-3b-ct2/

COPY token.txt ./
COPY hf_upload_model.py ./
RUN python hf_upload_model.py