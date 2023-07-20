mkdir michaelfeil
git lfs install --skip-smudge
git clone https://huggingface.co/michaelfeil/ct2fast-Llama-2-13b-hf michaelfeil/ct2fast-Llama-2-13b-hf
cp tokenizer.model michaelfeil/ct2fast-Llama-2-13b-hf
cd michaelfeil/ct2fast-Llama-2-13b-hf
git lfs pull
git lfs install --force
pwd
ls -l
