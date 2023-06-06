from huggingface_hub import HfApi, create_repo
import os

with open('token.txt', 'r') as f:
    token = f.read().rstrip("\n")

create_repo("limcheekin/falcon-7b-instruct-ct2",
            token=token,
            repo_type="model",
            exist_ok=True)
api = HfApi(token=token)
api.upload_folder(
    folder_path="tiiuae/falcon-7b-instruct-ct2",
    repo_id="limcheekin/falcon-7b-instruct-ct2",
)
