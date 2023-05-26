mkdir google
git lfs install --skip-smudge
git clone https://huggingface.co/google/flan-t5-xxl google/flan-t5-xxl
cd google/flan-t5-xxl
git lfs pull --include "*.model"
git lfs pull --include "*.bin"
git lfs install --force