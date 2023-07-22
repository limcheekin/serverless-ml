mkdir michaelfeil
git lfs install --skip-smudge
git clone https://huggingface.co/michaelfeil/ct2fast-Llama-2-13b-chat-hf michaelfeil/ct2fast-Llama-2-13b-chat-hf
cd michaelfeil/ct2fast-Llama-2-13b-chat-hf
git lfs pull
git lfs install --force
pwd
ls -l
