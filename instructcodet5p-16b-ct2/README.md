---
license: apache-2.0
language:
  - en
tags:
  - ctranslate2
  - flan-t5-xxl
  - quantization
  - int8
---

# Model Card for InstructCodeT5+ 16B Q8

The model is quantized version of the [Salesforce/instructcodet5p-16b](https://huggingface.co/Salesforce/instructcodet5p-16b) with int8 quantization.

## Model Details

### Model Description

The model being quantized using [CTranslate2](https://opennmt.net/CTranslate2/) with the following command:

```
ct2-transformers-converter --model Salesforce/instructcodet5p-16b --output_dir Salesforce/instructcodet5p-16b-ct2 --copy_files added_tokens.json merges.txt tokenizer.json tokenizer_config.json special_tokens_map.json vocab.json --quantization int8 --force --low_cpu_mem_usage
```

If you want to perform the quantization yourself, you need to install the following dependencies:

```
pip install -qU ctranslate2 transformers[torch] sentencepiece accelerate
```

- **Shared by:** Lim Chee Kin
- **License:** Apache 2.0

## How to Get Started with the Model

Use the code below to get started with the model.

```python
import ctranslate2
import transformers

translator = ctranslate2.Translator("limcheekin/instructcodet5p-16b-ct2")
tokenizer = transformers.AutoTokenizer.from_pretrained("limcheekin/instructcodet5p-16b-ct2")

input_text = "def print_hello_world():"
input_tokens = tokenizer.convert_ids_to_tokens(tokenizer.encode(input_text))

results = translator.translate_batch([input_tokens])

output_tokens = results[0].hypotheses[0]
output_text = tokenizer.decode(tokenizer.convert_tokens_to_ids(output_tokens))

print(output_text)
```

The code is taken from https://opennmt.net/CTranslate2/guides/transformers.html#t5.

The key method of the code above is `translate_batch`, you can find out [its supported parameters here](https://opennmt.net/CTranslate2/python/ctranslate2.Translator.html#ctranslate2.Translator.translate_batch).
