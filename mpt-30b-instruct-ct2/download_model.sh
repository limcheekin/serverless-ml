mkdir mosaicml
git lfs install --skip-smudge
git clone https://huggingface.co/mosaicml/mpt-30b-instruct mosaicml/mpt-30b-instruct
cd mosaicml/mpt-30b-instruct
git lfs pull
git lfs install --force
pwd
ls -l
