from src.qlora_training import run_qlora_simulation
from src.quantization import run_int4_quantization
from src.pruning import run_magnitude_pruning
from src.utils import create_project_outputs, save_compression_report

def main():
    create_project_outputs()

    qlora_metrics = run_qlora_simulation()
    quantization_metrics = run_int4_quantization()
    pruning_metrics = run_magnitude_pruning()

    final_metrics = {
        **qlora_metrics,
        **quantization_metrics,
        **pruning_metrics
    }

    save_compression_report(final_metrics)

    print("EdgeLM compression pipeline completed successfully.")
    print("Compression report saved inside outputs folder.")

if __name__ == "__main__":
    main()