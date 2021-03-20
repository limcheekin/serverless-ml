FROM public.ecr.aws/lambda/python:3.8

# Install OS packages for Pillow-SIMD
RUN yum -y install tar gzip zlib freetype-devel \
    gcc \
    ghostscript \
    lcms2-devel \
    libffi-devel \
    libimagequant-devel \
    libjpeg-devel \
    libraqm-devel \
    libtiff-devel \
    libwebp-devel \
    make \
    openjpeg2-devel \
    rh-python36 \
    rh-python36-python-virtualenv \
    sudo \
    tcl-devel \
    tk-devel \
    tkinter \
    which \
    xorg-x11-server-Xvfb \
    zlib-devel \
    && yum clean all

COPY app.py ./
COPY imagenet_class_index.json ./
COPY resnet50_weights_tf_dim_ordering_tf_kernels.h5 ./
COPY requirements.txt ./

RUN pip install -U pip setuptools wheel
RUN pip install -r requirements.txt

# Install Pillow-SIMD to take advantage of AVX2
RUN CC="cc -mavx2" pip install -U --force-reinstall pillow-simd

CMD ["app.handler"]
