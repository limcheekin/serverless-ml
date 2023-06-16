from huggingface_hub import HfApi, create_repo
import os

with open('token.txt', 'r') as f:
    token = f.read().rstrip("\n")

create_repo("limcheekin/h2ogpt-gm-oasst1-en-2048-falcon-7b-ct2",
            token=token,
            repo_type="model",
            exist_ok=True)
api = HfApi(token=token)
api.upload_folder(
    folder_path="h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b-ct2",
    repo_id="limcheekin/h2ogpt-gm-oasst1-en-2048-falcon-7b-ct2",
)
