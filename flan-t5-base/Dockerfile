# REF: https://aws.amazon.com/blogs/machine-learning/using-container-images-to-run-pytorch-models-in-aws-lambda/
# REF: https://heidloff.net/article/running-llm-flan-t5-locally/
FROM public.ecr.aws/lambda/python:3.10

COPY app.py ./

RUN pip install -U pip setuptools wheel
RUN pip install transformers
RUN pip install transformers[torch]
RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

# Load the model related files from Huggingface and store it in the model directory
RUN mkdir model
RUN curl -L https://huggingface.co/google/flan-t5-base/resolve/main/pytorch_model.bin -o ./model/pytorch_model.bin
RUN curl https://huggingface.co/google/flan-t5-base/raw/main/config.json -o ./model/config.json
RUN curl https://huggingface.co/google/flan-t5-base/raw/main/generation_config.json -o ./model/generation_config.json

RUN curl https://huggingface.co/google/flan-t5-base/raw/main/tokenizer.json -o ./model/tokenizer.json
RUN curl https://huggingface.co/google/flan-t5-base/raw/main/tokenizer_config.json -o ./model/tokenizer_config.json
RUN curl https://huggingface.co/google/flan-t5-base/raw/main/special_tokens_map.json -o ./model/special_tokens_map.json
RUN curl https://huggingface.co/google/flan-t5-base/resolve/main/spiece.model -o ./model/spiece.model

CMD ["app.handler"]
