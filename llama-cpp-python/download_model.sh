git lfs install --skip-smudge
git clone https://huggingface.co/vihangd/open_llama_7b_300bt_ggml model
cd model
git lfs pull --include "ggml-model-q4_0.bin"
git lfs install --force