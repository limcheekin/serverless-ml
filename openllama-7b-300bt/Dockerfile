# REF: https://aws.amazon.com/blogs/machine-learning/using-container-images-to-run-pytorch-models-in-aws-lambda/
# REF: https://heidloff.net/article/running-llm-flan-t5-locally/
FROM public.ecr.aws/lambda/python:3.10

COPY app.py ./

RUN pip install -U pip setuptools wheel
RUN pip install llama-cpp-python

# Load the model related files from Huggingface and store it in the model directory
RUN mkdir model
RUN curl -L https://huggingface.co/vihangd/open_llama_7b_300bt_ggml/resolve/main/ggml-model-q8_0.bin -o ./model/openllama-7b-300bt-ggml-q8_0.bin

CMD ["app.handler"]
