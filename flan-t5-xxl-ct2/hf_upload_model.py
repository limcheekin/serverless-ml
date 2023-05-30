from huggingface_hub import HfApi, create_repo
import os

with open('token.txt') as f:
    token = f.read()

create_repo("limcheekin/flan-t5-xxl-ct2",
            token=token,
            repo_type="model",
            exist_ok=True)
api = HfApi(token=token)
api.upload_folder(
    folder_path="google/flan-t5-xxl-ct2",
    repo_id="limcheekin/flan-t5-xxl-ct2",
)
