mkdir mosaicml
git lfs install --skip-smudge
git clone https://huggingface.co/michaelfeil/ct2fast-mpt-30b-instruct mosaicml/mpt-30b-instruct-ct2
cd mosaicml/mpt-30b-instruct-ct2
git lfs pull
git lfs install --force
pwd
ls -l
