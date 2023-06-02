mkdir mosaicml
git lfs install
git clone https://huggingface.co/mosaicml/mpt-7b-storywriter mosaicml/mpt-7b-storywriter
cd mosaicml/mpt-7b-storywriter
git lfs pull
pwd
ls -l

mkdir -p EleutherAI/gpt-neox-20b
curl https://huggingface.co/EleutherAI/gpt-neox-20b/raw/main/tokenizer_config.json -o EleutherAI/gpt-neox-20b/tokenizer_config.json
curl https://huggingface.co/EleutherAI/gpt-neox-20b/raw/main/vocab.json -o EleutherAI/gpt-neox-20b/vocab.json
curl https://huggingface.co/EleutherAI/gpt-neox-20b/raw/main/merges.txt -o EleutherAI/gpt-neox-20b/merges.txt
curl https://huggingface.co/EleutherAI/gpt-neox-20b/resolve/main/tokenizer.json -o EleutherAI/gpt-neox-20b/tokenizer.json
curl https://huggingface.co/EleutherAI/gpt-neox-20b/resolve/main/special_tokens_map.json -o EleutherAI/gpt-neox-20b/special_tokens_map.json