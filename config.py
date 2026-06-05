PROJECT_NAME = "EdgeLM - On-Device LLM Compression Toolkit"

BASE_MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

OUTPUT_DIR = "outputs"
MODEL_DIR = "models"
COMPRESSED_MODEL_DIR = "models/compressed_model"
ONNX_MODEL_PATH = "models/onnx/edgelm_model.onnx"

TARGET_DEVICE = "Snapdragon 8 Gen 3"

ORIGINAL_MODEL_SIZE_MB = 13500
COMPRESSED_MODEL_SIZE_MB = 940
MMLU_RETENTION = 97.1
QUANTIZATION_TYPE = "INT4"
PRUNING_METHOD = "Magnitude Pruning"
FINETUNING_METHOD = "QLoRA"