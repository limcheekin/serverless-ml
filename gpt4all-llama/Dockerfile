FROM public.ecr.aws/lambda/python:3.10

RUN yum -y install wget

RUN wget https://huggingface.co/LLukas22/gpt4all-lora-quantized-ggjt/resolve/main/ggjt-model.bin

COPY app.py ./
COPY requirements.txt ./

RUN pip install -U pip setuptools wheel
RUN pip install -r requirements.txt

CMD ["app.handler"]
