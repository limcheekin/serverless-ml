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
RUN curl -L https://huggingface.co/vblagoje/bart_lfqa/resolve/main/pytorch_model.bin -o ./model/pytorch_model.bin
RUN curl https://huggingface.co/vblagoje/bart_lfqa/raw/main/config.json -o ./model/config.json
RUN curl https://huggingface.co/vblagoje/bart_lfqa/raw/main/merges.txt -o ./model/merges.txt

RUN curl https://huggingface.co/vblagoje/bart_lfqa/raw/main/tokenizer.json -o ./model/tokenizer.json
RUN curl https://huggingface.co/vblagoje/bart_lfqa/raw/main/tokenizer_config.json -o ./model/tokenizer_config.json
RUN curl https://huggingface.co/vblagoje/bart_lfqa/raw/main/vocab.json -o ./model/vocab.json

CMD ["app.handler"]
