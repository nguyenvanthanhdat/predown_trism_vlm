import os

docker_image = os.getenv(
    "DOCKER_IMAGE", 
    "nvcr.io/nvidia/tritonserver:24.12-vllm-python-py3"
)
hf_token   = os.getenv("HF_TOKEN", "")
repo_name = os.getenv("REPO_NAME", "")
model_name = os.getenv("MODEL_NAME", "")

# file_info = f"""FROM {docker_image}

# COPY {model_name} /weights/{model_name}"""

file_info = f"""FROM {docker_image}

COPY download.py /workspace/download.py
RUN pip install huggingface-hub
RUN python3 /workspace/download.py"""
# Write the Dockerfile


with open("Dockerfile", "w") as f:
    f.write(file_info)
    print(f"Written Dockerfile information !!!")