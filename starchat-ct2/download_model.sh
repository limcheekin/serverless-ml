mkdir michaelfeil
git lfs install --skip-smudge
git clone https://huggingface.co/michaelfeil/ct2fast-starchat-beta michaelfeil/ct2fast-starchat-beta
cd michaelfeil/ct2fast-starchat-beta
git lfs pull
git lfs install --force
pwd
ls -l
