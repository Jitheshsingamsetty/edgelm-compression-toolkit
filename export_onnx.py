from src.onnx_export import export_model_to_onnx

def main():
    export_model_to_onnx()
    print("ONNX export process completed successfully.")

if __name__ == "__main__":
    main()