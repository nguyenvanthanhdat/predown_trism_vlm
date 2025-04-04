import os

docker_image = os.getenv(
    "DOCKER_IMAGE", 
    "nvcr.io/nvidia/tritonserver:24.12-vllm-python-py3"
)
hf_token   = os.getenv("HF_TOKEN", "")
model_name = os.getenv("MODEL_NAME", "")

file_info = f"""FROM {docker_image}

COPY {model_name} /weights/{model_name}"""

with open("Dockerfile", "w") as f:
    f.write(file_info)
    print(f"Written Dockerfile information !!!")