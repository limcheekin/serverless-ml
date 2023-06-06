---
license: apache-2.0
language:
  - en
tags:
  - ctranslate2
  - falcon-7b-instruct
  - quantization
  - int8
---

# Falcon-7B-Instruct Q8

The model is quantized version of the [tiiuae/falcon-7b-instruct](https://huggingface.co/tiiuae/falcon-7b-instruct) with int8 quantization.

## Model Details

### Model Description

The model being quantized using [CTranslate2](https://opennmt.net/CTranslate2/) with the following command:

```
ct2-transformers-converter --model tiiuae/falcon-7b-instruct --output_dir tiiuae/falcon-7b-instruct-ct2 --copy_files tokenizer.json tokenizer_config.json special_tokens_map.json generation_config.json --quantization int8 --force --low_cpu_mem_usage --trust_remote_code
```

If you want to perform the quantization yourself, you need to install the following dependencies:

```
pip install -qU ctranslate2 transformers[torch] accelerate einops
```

- **Shared by:** Lim Chee Kin
- **License:** Apache 2.0

## How to Get Started with the Model

Use the code below to get started with the model.

```python
import ctranslate2
import transformers

generator = ctranslate2.Generator("limcheekin/falcon-7b-instruct-ct2")
tokenizer = transformers.AutoTokenizer.from_pretrained("limcheekin/falcon-7b-instruct-ct2")

prompt = "Long long time ago, "
tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(prompt))

results = generator.generate_batch([tokens], max_length=256, sampling_topk=10)

text = tokenizer.decode(results[0].sequences_ids[0])
```

The code is taken from https://opennmt.net/CTranslate2/guides/transformers.html#mpt.

The key method of the code above is `generate_batch`, you can find out [its supported parameters here](https://opennmt.net/CTranslate2/python/ctranslate2.Generator.html#ctranslate2.Generator.generate_batch).
