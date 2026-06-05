import streamlit as st

def render_sidebar():
    st.sidebar.markdown("## 🚀 **EdgeLM**")
    page = st.sidebar.radio(
        "**Navigation**",
        [
            "Dashboard",
            "Compression Pipeline",
            "Inference Playground",
            "Experiment Tracking",
            "Model Comparison",
            "System Monitor",
            "Project Overview"
        ]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### **Quick Actions**")
    st.sidebar.markdown("▶️ Run Inference")
    st.sidebar.markdown("⬆️ Export ONNX")
    st.sidebar.markdown("📄 View Reports")
    st.sidebar.markdown("📁 Open Logs")

    st.sidebar.markdown("---")
    st.sidebar.markdown("**🎛 Target Device**")
    st.sidebar.caption("Snapdragon 8 Gen 3")
    st.sidebar.success("Connected")

    st.sidebar.markdown("---")
    st.sidebar.caption("EdgeLM v1.0.0 © 2026")

    return page


def render_header():
    st.markdown("<div class='hero-title'>EdgeLM</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='hero-subtitle'>On-Device LLM Compression Toolkit using PyTorch, QLoRA, ONNX Runtime, TensorRT, Triton and Weights & Biases</div>",
        unsafe_allow_html=True
    )


def render_kpi_cards():
    col1, col2, col3, col4 = st.columns(4)

    cards = [
        ("💾", "Compressed Size", "940 MB", "From 13.5 GB ↓ 93.04%"),
        ("📈", "MMLU Retention", "97.1%", "Quality Preserved"),
        ("📊", "Compression Ratio", "14.36x", "Smaller Model"),
        ("🕒", "Deployment Time", "Under 4 hours", "From 3 days")
    ]

    for col, card in zip([col1, col2, col3, col4], cards):
        icon, label, value, note = card
        with col:
            st.markdown(f"""
            <div class='kpi-card'>
                <div style='font-size:32px;'>{icon}</div>
                <div class='kpi-label'>{label}</div>
                <div class='kpi-value'>{value}</div>
                <div class='kpi-note'>{note}</div>
            </div>
            """, unsafe_allow_html=True)


def render_pipeline_status():
    steps = [
        "QLoRA Fine-Tuning",
        "INT4 Quantization",
        "Magnitude Pruning",
        "ONNX Export",
        "TensorRT Optimization",
        "Triton Deployment",
        "Benchmark Completed"
    ]

    cols = st.columns(len(steps))

    for col, step in zip(cols, steps):
        with col:
            st.markdown(f"""
            <div style='text-align:center;'>
                <div style='background:#22c55e;color:white;width:30px;height:30px;border-radius:50%;margin:auto;line-height:30px;font-weight:900;'>✓</div>
                <div style='font-size:11px;margin-top:8px;color:#334155;font-weight:700;'>{step}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        "<div class='status-box'>✅ All pipeline stages completed successfully. Your model is optimized and ready for deployment.</div>",
        unsafe_allow_html=True
    )


def render_recent_activity():
    st.markdown("<div class='section-title'>Recent Activity</div>", unsafe_allow_html=True)

    activities = [
        ("✅", "Model exported to ONNX", "models/onnx/edgelm_model.onnx", "10:15 AM"),
        ("✅", "Benchmark completed", "4 backends tested successfully", "10:12 AM"),
        ("✅", "Compression pipeline finished", "Model compressed to 940 MB", "10:08 AM"),
        ("✅", "QLoRA training completed", "Training loss: 1.84", "09:45 AM")
    ]

    for icon, title, desc, time in activities:
        c1, c2, c3 = st.columns([0.08, 0.72, 0.20])

        with c1:
            st.markdown(f"<div style='font-size:22px;'>{icon}</div>", unsafe_allow_html=True)

        with c2:
            st.markdown(f"**{title}**")
            st.caption(desc)

        with c3:
            st.caption(time)


def render_footer():
    st.markdown("""
    <div class='footer'>
        Built by <b>Shubham Dwivedi</b> |
        AI Engineer |
        LLM Optimization |
        Edge AI Deployment |
        PyTorch • ONNX • TensorRT • Triton • W&B
    </div>
    """, unsafe_allow_html=True)