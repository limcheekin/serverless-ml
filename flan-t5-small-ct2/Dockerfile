# REF: https://aws.amazon.com/blogs/machine-learning/using-container-images-to-run-pytorch-models-in-aws-lambda/
# REF: https://heidloff.net/article/running-llm-flan-t5-locally/
FROM public.ecr.aws/lambda/python:3.10

COPY app.py ./
COPY hf_upload_model.py ./

RUN pip install -U pip setuptools wheel
RUN pip install transformers ctranslate2 sentencepiece
RUN pip install torch --extra-index-url https://download.pytorch.org/whl/cpu

# Load the model related files from Huggingface and store it in the model directory
RUN mkdir -p google/flan-t5-small
RUN curl -L https://huggingface.co/google/flan-t5-small/resolve/main/pytorch_model.bin -o ./google/flan-t5-small/pytorch_model.bin
RUN curl https://huggingface.co/google/flan-t5-small/raw/main/config.json -o ./google/flan-t5-small/config.json
RUN curl https://huggingface.co/google/flan-t5-small/raw/main/generation_config.json -o ./google/flan-t5-small/generation_config.json

RUN curl https://huggingface.co/google/flan-t5-small/raw/main/tokenizer.json -o ./google/flan-t5-small/tokenizer.json
RUN curl https://huggingface.co/google/flan-t5-small/raw/main/tokenizer_config.json -o ./google/flan-t5-small/tokenizer_config.json
RUN curl https://huggingface.co/google/flan-t5-small/raw/main/special_tokens_map.json -o ./google/flan-t5-small/special_tokens_map.json
RUN curl -L https://huggingface.co/google/flan-t5-small/resolve/main/spiece.model -o ./google/flan-t5-small/spiece.model
            
RUN ct2-transformers-converter --model google/flan-t5-small --output_dir google/flan-t5-small-ct2 --quantization int8 --force && \
    cp google/flan-t5-small/tokenizer.json google/flan-t5-small-ct2/ && \
    cp google/flan-t5-small/tokenizer_config.json google/flan-t5-small-ct2/ && \
    cp google/flan-t5-small/special_tokens_map.json google/flan-t5-small-ct2/ && \
    cp google/flan-t5-small/spiece.model google/flan-t5-small-ct2/

COPY README.md google/flan-t5-small-ct2/

RUN python hf_upload_model.py && \
    rm -rf google/flan-t5-small

CMD ["app.handler"]
