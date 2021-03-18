FROM public.ecr.aws/lambda/python:3.8

COPY app.py ./
COPY imagenet_class_index.json ./
COPY resnet50_weights_tf_dim_ordering_tf_kernels.h5 ./

RUN pip install -U pip setuptools wheel
RUN pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.4.0-cp38-cp38-manylinux2010_x86_64.whl
RUN pip install keras pillow

CMD ["app.handler"]
