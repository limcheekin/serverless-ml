mkdir tiiuae
git lfs install --skip-smudge
git clone https://huggingface.co/michaelfeil/ct2fast-falcon-40b-instruct tiiuae/falcon-40b-instruct-ct2
cd tiiuae/falcon-40b-instruct-ct2
git lfs pull
git lfs install --force
pwd
ls -l
