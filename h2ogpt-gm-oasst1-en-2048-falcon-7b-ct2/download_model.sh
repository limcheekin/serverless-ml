mkdir h2oai
git lfs install --skip-smudge
git clone https://huggingface.co/h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b-v3 h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b
cd h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b
git lfs pull
git lfs install --force
pwd
ls -l
