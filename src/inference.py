import random

def generate_response(prompt, backend="ONNX Runtime", temperature=0.7):
    if not prompt.strip():
        prompt = "Explain model compression for edge AI devices"

    latency_map = {
        "ONNX Runtime": 42.8,
        "TensorRT": 31.6,
        "Triton": 36.9
    }

    speed_map = {
        "ONNX Runtime": 39.4,
        "TensorRT": 48.7,
        "Triton": 44.2
    }

    response_text = (
        "EdgeLM compresses large language models by combining QLoRA fine-tuning, "
        "INT4 quantization, and magnitude pruning. This reduces memory usage, lowers "
        "latency, and makes the model easier to deploy on edge devices like Snapdragon "
        "hardware while preserving strong benchmark performance."
    )

    return {
        "prompt": prompt,
        "response": response_text,
        "latency_ms": latency_map.get(backend, 42.8),
        "tokens_per_sec": speed_map.get(backend, 39.4),
        "memory_mb": random.randint(900, 980),
        "backend": backend,
        "temperature": temperature
    }