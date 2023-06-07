mkdir michaelfeil
git lfs install --skip-smudge
git clone https://huggingface.co/michaelfeil/ct2fast-starcoder michaelfeil/ct2fast-starcoder
cd michaelfeil/ct2fast-starcoder
git lfs pull
git lfs install --force
pwd
ls -l
