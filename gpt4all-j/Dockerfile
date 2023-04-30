# REF: https://aws.amazon.com/blogs/machine-learning/using-container-images-to-run-pytorch-models-in-aws-lambda/
# REF: https://heidloff.net/article/running-llm-flan-t5-locally/
FROM public.ecr.aws/lambda/python:3.10

COPY app.py ./

RUN pip install -U pip setuptools wheel
RUN pip install gpt4all-j

# download the model file
RUN mkdir model
RUN curl -L https://gpt4all.io/models/ggml-gpt4all-j.bin -o ./model/ggml-gpt4all-j

CMD ["app.handler"]
