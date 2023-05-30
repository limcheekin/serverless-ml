import ctranslate2

model_name_or_path = "Salesforce/instructcodet5p-16b"
output_dir = "Salesforce/instructcodet5p-16b-ct2"
copy_files = "added_tokens.json merges.txt tokenizer.json tokenizer_config.json special_tokens_map.json vocab.json".split(
    " ")

ct = ctranslate2.converters.TransformersConverter(
    model_name_or_path=model_name_or_path, low_cpu_mem_usage=True, trust_remote_code=True)
ct.convert(output_dir=output_dir, quantization="int8", force=True)
