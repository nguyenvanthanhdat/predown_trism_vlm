from huggingface_hub import snapshot_download
import os

hf_token   = os.getenv("HF_TOKEN", "")
# model_name = os.getenv("MODEL_NAME", "")
# model_path = model_name.split("/")[-1]
repo_name = os.getenv("REPO_NAME", "")
model_name = os.getenv("MODEL_NAME", repo_name)

# Download the model
snapshot_download(
    # repo_id="casperhansen/llama-3-8b-instruct-awq",
    repo_id=f"{repo_name}/{model_name}",
    revision="main",
    cache_dir=model_name,
    local_dir=model_name,
    local_dir_use_symlinks=False,
    resume_download=True,
    token=hf_token,
)
