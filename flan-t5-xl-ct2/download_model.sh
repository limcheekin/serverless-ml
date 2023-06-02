mkdir -p google/flan-t5-xl
curl -L https://huggingface.co/google/flan-t5-xl/resolve/main/pytorch_model-00001-of-00002.bin -o ./google/flan-t5-xl/pytorch_model-00001-of-00002.bin
curl -L https://huggingface.co/google/flan-t5-xl/resolve/main/pytorch_model-00002-of-00002.bin -o ./google/flan-t5-xl/pytorch_model-00002-of-00002.bin
curl https://huggingface.co/google/flan-t5-xl/raw/main/pytorch_model.bin.index.json -o ./google/flan-t5-xl/pytorch_model.bin.index.json
curl https://huggingface.co/google/flan-t5-xl/raw/main/config.json -o ./google/flan-t5-xl/config.json
curl https://huggingface.co/google/flan-t5-xl/raw/main/generation_config.json -o ./google/flan-t5-xl/generation_config.json

curl https://huggingface.co/google/flan-t5-xl/raw/main/tokenizer.json -o ./google/flan-t5-xl/tokenizer.json
curl https://huggingface.co/google/flan-t5-xl/raw/main/tokenizer_config.json -o ./google/flan-t5-xl/tokenizer_config.json
curl https://huggingface.co/google/flan-t5-xl/raw/main/special_tokens_map.json -o ./google/flan-t5-xl/special_tokens_map.json
curl -L https://huggingface.co/google/flan-t5-xl/resolve/main/spiece.model -o ./google/flan-t5-xl/spiece.model
