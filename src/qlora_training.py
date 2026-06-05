from config import FINETUNING_METHOD, BASE_MODEL_NAME

def run_qlora_simulation():
    metrics = {
        "Base Model": BASE_MODEL_NAME,
        "Fine Tuning Method": FINETUNING_METHOD,
        "LoRA Rank": 8,
        "LoRA Alpha": 16,
        "Trainable Parameters": "0.42%",
        "Training Loss": 1.84,
        "Validation Loss": 1.91
    }

    return metrics