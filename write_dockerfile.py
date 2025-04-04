import os

docker_image = os.getenv(
    "DOCKER_IMAGE", 
    "nvcr.io/nvidia/tritonserver:24.12-vllm-python-py3"
)
hf_token   = os.getenv("HF_TOKEN", "")
model_name = os.getenv("MODEL_NAME", "")

model_path = model_name.split("/")[-1]


file_info = f"""FROM {docker_image}

COPY {model_path} /weights/{model_path}"""

with open("Dockerfile", "w") as f:
    f.write(file_info)
    print(f"Written Dockerfile information !!!")