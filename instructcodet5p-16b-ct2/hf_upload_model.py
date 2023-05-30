from huggingface_hub import HfApi, create_repo
import os

with open('token.txt', 'r') as f:
    token = f.read().rstrip("\n")

create_repo("limcheekin/instructcodet5p-16b-ct2",
            token=token,
            repo_type="model",
            exist_ok=True)
api = HfApi(token=token)
api.upload_folder(
    folder_path="Salesforce/instructcodet5p-16b-ct2",
    repo_id="limcheekin/instructcodet5p-16b-ct2",
)
