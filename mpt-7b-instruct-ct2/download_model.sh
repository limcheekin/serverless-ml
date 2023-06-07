mkdir mosaicml
git lfs install --skip-smudge
git clone https://huggingface.co/mosaicml/mpt-7b-instruct mosaicml/mpt-7b-instruct
cd mosaicml/mpt-7b-instruct
git lfs pull
git lfs install --force
pwd
ls -l
