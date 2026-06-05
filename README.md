# EdgeLM - On-Device LLM Compression Toolkit

EdgeLM is a portfolio-ready AI engineering project that demonstrates an on-device LLM compression workflow using QLoRA, INT4 quantization, magnitude pruning, ONNX Runtime, TensorRT, Triton Inference Server, and Weights & Biases.

## Features

- QLoRA-based fine-tuning simulation
- INT4 quantization workflow
- Magnitude pruning simulation
- ONNX export placeholder
- Backend latency, memory, and throughput benchmarking
- Streamlit dashboard with interactive charts
- Portfolio-ready project structure

## Tech Stack

- Python
- PyTorch
- QLoRA
- ONNX Runtime
- TensorRT
- Triton
- Streamlit
- Plotly
- Pandas
- Weights & Biases

## Project Workflow

1. Load base LLM
2. Apply QLoRA fine-tuning
3. Apply INT4 quantization
4. Apply magnitude pruning
5. Export model to ONNX
6. Benchmark across backends
7. Visualize results in Streamlit dashboard

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt