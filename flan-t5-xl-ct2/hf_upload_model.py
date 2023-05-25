from huggingface_hub import HfApi, create_repo
import os

create_repo("limcheekin/flan-t5-xl-ct2",
            token=os.environ["HF_TOKEN"],
            repo_type="model",
            exist_ok=True)
api = HfApi(token=os.environ["HF_TOKEN"])
api.upload_folder(
    folder_path="google/flan-t5-xl-ct2",
    repo_id="limcheekin/flan-t5-xl-ct2",
)
