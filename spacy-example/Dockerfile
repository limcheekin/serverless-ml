FROM public.ecr.aws/lambda/python:3.8

COPY app.py ./
COPY requirements.txt ./

RUN pip install -U pip setuptools wheel
RUN pip install -r requirements.txt

CMD ["app.handler"]
