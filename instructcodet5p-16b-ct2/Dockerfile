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
RUN ct2-transformers-converter --model Salesforce/instructcodet5p-16b --output_dir Salesforce/instructcodet5p-16b-ct2 --copy_files added_tokens.json merges.txt tokenizer.json tokenizer_config.json special_tokens_map.json vocab.json --quantization int8 --force --low_cpu_mem_usage && \
    rm -rf Salesforce/instructcodet5p-16b

COPY README.md Salesforce/instructcodet5p-16b-ct2/

COPY token.txt ./
COPY hf_upload_model.py ./
RUN python hf_upload_model.py