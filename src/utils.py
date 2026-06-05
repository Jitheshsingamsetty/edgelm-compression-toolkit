import os
import pandas as pd
from config import OUTPUT_DIR

def create_project_outputs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs("outputs/charts", exist_ok=True)
    os.makedirs("outputs/logs", exist_ok=True)
    os.makedirs("models/compressed_model", exist_ok=True)
    os.makedirs("models/onnx", exist_ok=True)

def save_compression_report(metrics):
    df = pd.DataFrame([metrics])
    df.to_csv("outputs/compression_metrics.csv", index=False)

    with open("outputs/evaluation_report.txt", "w", encoding="utf-8") as file:
        file.write("EdgeLM Compression Evaluation Report\n")
        file.write("=" * 45 + "\n\n")

        for key, value in metrics.items():
            file.write(f"{key}: {value}\n")