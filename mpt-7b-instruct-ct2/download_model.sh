mkdir mosaicml
git lfs install --skip-smudge
git clone https://huggingface.co/mosaicml/mpt-7b-instruct mosaicml/mpt-7b-instruct
cd mosaicml/mpt-7b-instruct
git lfs pull
git lfs install --force
pwd
ls -l

mkdir -p /EleutherAI/gpt-neox-20b
curl https://huggingface.co/EleutherAI/gpt-neox-20b/resolve/main/config.json -o /EleutherAI/gpt-neox-20b/config.json
curl https://huggingface.co/EleutherAI/gpt-neox-20b/resolve/main/tokenizer_config.json -o /EleutherAI/gpt-neox-20b/tokenizer_config.json
curl https://huggingface.co/EleutherAI/gpt-neox-20b/resolve/main/vocab.json -o /EleutherAI/gpt-neox-20b/vocab.json
curl https://huggingface.co/EleutherAI/gpt-neox-20b/resolve/main/merges.txt -o /EleutherAI/gpt-neox-20b/merges.txt
curl https://huggingface.co/EleutherAI/gpt-neox-20b/resolve/main/tokenizer.json -o /EleutherAI/gpt-neox-20b/tokenizer.json
curl https://huggingface.co/EleutherAI/gpt-neox-20b/resolve/main/special_tokens_map.json -o /EleutherAI/gpt-neox-20b/special_tokens_map.json
cd /EleutherAI/gpt-neox-20b
pwd
ls -l