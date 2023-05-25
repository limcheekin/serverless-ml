mkdir -p google/flan-t5-xxl
curl -L https://huggingface.co/google/flan-t5-xxl/resolve/main/pytorch_model-00001-of-00005.bin -o ./google/flan-t5-xxl/pytorch_model-00001-of-00005.bin
curl -L https://huggingface.co/google/flan-t5-xxl/resolve/main/pytorch_model-00002-of-00005.bin -o ./google/flan-t5-xxl/pytorch_model-00002-of-00005.bin
curl -L https://huggingface.co/google/flan-t5-xxl/resolve/main/pytorch_model-00003-of-00005.bin -o ./google/flan-t5-xxl/pytorch_model-00003-of-00005.bin
curl -L https://huggingface.co/google/flan-t5-xxl/resolve/main/pytorch_model-00004-of-00005.bin -o ./google/flan-t5-xxl/pytorch_model-00004-of-00005.bin
curl -L https://huggingface.co/google/flan-t5-xxl/resolve/main/pytorch_model-00005-of-00005.bin -o ./google/flan-t5-xxl/pytorch_model-00005-of-00005.bin
curl https://huggingface.co/google/flan-t5-xxl/raw/main/pytorch_model.bin.index.json -o ./google/flan-t5-xxl/pytorch_model.bin.index.json
curl https://huggingface.co/google/flan-t5-xxl/raw/main/config.json -o ./google/flan-t5-xxl/config.json
curl https://huggingface.co/google/flan-t5-xxl/raw/main/generation_config.json -o ./google/flan-t5-xxl/generation_config.json

curl https://huggingface.co/google/flan-t5-xxl/raw/main/tokenizer.json -o ./google/flan-t5-xxl/tokenizer.json
curl https://huggingface.co/google/flan-t5-xxl/raw/main/tokenizer_config.json -o ./google/flan-t5-xxl/tokenizer_config.json
curl https://huggingface.co/google/flan-t5-xxl/raw/main/special_tokens_map.json -o ./google/flan-t5-xxl/special_tokens_map.json
curl -L https://huggingface.co/google/flan-t5-xxl/resolve/main/spiece.model -o ./google/flan-t5-xxl/spiece.model
