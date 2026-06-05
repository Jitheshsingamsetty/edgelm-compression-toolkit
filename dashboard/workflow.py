import streamlit as st

def render_workflow():
    st.markdown("<div class='section-title'>🚀 Compression Pipeline</div>", unsafe_allow_html=True)

    graph = """
    digraph {
        rankdir=LR;
        graph [bgcolor="transparent", pad="0.4", nodesep="0.55", ranksep="0.7"];

        node [
            shape=box
            style="rounded,filled"
            fillcolor="#6d5dfc"
            color="#6d5dfc"
            fontcolor="white"
            fontsize=13
            margin="0.18,0.12"
        ];

        edge [color="#334155", penwidth=2];

        A [label="LLaMA-2 7B"];
        B [label="QLoRA"];
        C [label="INT4 Quantization"];
        D [label="Magnitude Pruning"];
        E [label="ONNX Export"];
        F [label="TensorRT"];
        G [label="Triton"];
        H [label="Snapdragon 8 Gen 3"];

        A -> B;
        B -> C;
        C -> D;
        D -> E;
        E -> F;
        E -> G;
        F -> H;
        G -> H;
    }
    """

    st.graphviz_chart(graph, use_container_width=True)

def render_architecture():
    st.markdown("<div class='section-title'>🧠 EdgeLM Architecture</div>", unsafe_allow_html=True)

    graph = """
    digraph {
        rankdir=TB;
        graph [bgcolor="transparent", pad="0.5", nodesep="0.55", ranksep="0.6"];

        node [
            shape=box
            style="rounded,filled"
            fillcolor="#6d5dfc"
            color="#6d5dfc"
            fontcolor="white"
            fontsize=13
            margin="0.22,0.14"
        ];

        edge [color="#334155", penwidth=2];

        A [label="Base LLM\\nLLaMA-2 7B"];
        B [label="QLoRA Fine-Tuning"];
        C [label="INT4 Quantization"];
        D [label="Magnitude Pruning"];
        E [label="ONNX Export"];
        F [label="ONNX Runtime"];
        G [label="TensorRT"];
        H [label="Triton Server"];
        I [label="Edge Device\\nSnapdragon 8 Gen 3"];

        A -> B;
        B -> C;
        C -> D;
        D -> E;
        E -> F;
        E -> G;
        E -> H;
        F -> I;
        G -> I;
        H -> I;
    }
    """

    st.graphviz_chart(graph, use_container_width=True)