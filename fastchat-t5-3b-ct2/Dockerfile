# REF: https://aws.amazon.com/blogs/machine-learning/using-container-images-to-run-pytorch-models-in-aws-lambda/
# REF: https://heidloff.net/article/running-llm-flan-t5-locally/
FROM public.ecr.aws/lambda/python:3.10

COPY app.py ./
RUN mkdir lmsys
COPY fastchat-t5-3b ./lmsys/

RUN pip install -U pip setuptools wheel
RUN pip install transformers ctranslate2 sentencepiece
RUN pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
        
RUN ct2-transformers-converter --model lmsys/fastchat-t5-3b --output_dir lmsys/fastchat-t5-3b-ct2 --quantization int8

RUN rm lmsys/fastchat-t5-3b/pytorch_model.bin

CMD ["app.handler"]
