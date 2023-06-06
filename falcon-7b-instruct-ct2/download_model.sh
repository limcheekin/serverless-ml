mkdir tiiuae
git lfs install --skip-smudge
git clone https://huggingface.co/tiiuae/falcon-7b-instruct tiiuae/falcon-7b-instruct
cd tiiuae/falcon-7b-instruct
git lfs pull
git lfs install --force
pwd
ls -l
