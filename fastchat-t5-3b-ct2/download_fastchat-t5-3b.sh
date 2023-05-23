mkdir -p lmsys/fastchat-t5-3b
curl -L https://huggingface.co/lmsys/fastchat-t5-3b-v1.0/resolve/main/pytorch_model.bin -o ./lmsys/fastchat-t5-3b/pytorch_model.bin
curl https://huggingface.co/lmsys/fastchat-t5-3b-v1.0/raw/main/config.json -o ./lmsys/fastchat-t5-3b/config.json
curl https://huggingface.co/lmsys/fastchat-t5-3b-v1.0/raw/main/generation_config.json -o ./lmsys/fastchat-t5-3b/generation_config.json
curl https://huggingface.co/lmsys/fastchat-t5-3b-v1.0/raw/main/added_tokens.json -o ./lmsys/fastchat-t5-3b/added_tokens.json

curl https://huggingface.co/lmsys/fastchat-t5-3b-v1.0/raw/main/pytorch_model.bin.index.json -o ./lmsys/fastchat-t5-3b/pytorch_model.bin.index.json
curl https://huggingface.co/lmsys/fastchat-t5-3b-v1.0/raw/main/tokenizer_config.json -o ./lmsys/fastchat-t5-3b/tokenizer_config.json
curl https://huggingface.co/lmsys/fastchat-t5-3b-v1.0/raw/main/special_tokens_map.json -o ./lmsys/fastchat-t5-3b/special_tokens_map.json
curl -L https://huggingface.co/lmsys/fastchat-t5-3b-v1.0/resolve/main/spiece.model -o ./lmsys/fastchat-t5-3b/spiece.model
