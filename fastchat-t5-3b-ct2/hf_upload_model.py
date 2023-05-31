from huggingface_hub import HfApi, create_repo
import os

with open('token.txt', 'r') as f:
    token = f.read().rstrip("\n")

create_repo("limcheekin/fastchat-t5-3b-ct2",
            token=token,
            repo_type="model",
            exist_ok=True)
api = HfApi(token=token)
api.upload_folder(
    folder_path="lmsys/fastchat-t5-3b-ct2",
    repo_id="limcheekin/fastchat-t5-3b-ct2",
)
