import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def apply_chart_theme(fig):
    fig.update_layout(
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(color="#0f172a", size=12),
        title_font=dict(color="#0f172a", size=16),
        xaxis=dict(color="#334155", gridcolor="#e2e8f0"),
        yaxis=dict(color="#334155", gridcolor="#e2e8f0"),
        legend=dict(font=dict(color="#334155")),
        margin=dict(l=30, r=30, t=55, b=30)
    )
    return fig

def render_model_size_chart():
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["Original LLaMA-2 7B", "Compressed EdgeLM"],
        y=[13500, 940],
        text=["13,500", "940"],
        textposition="outside",
        marker_color=["#6d5dfc", "#22c55e"],
        name="Size MB"
    ))

    fig.update_layout(
        title="Model Size Before vs After Compression",
        yaxis_title="Size (MB)",
        showlegend=False,
        height=330
    )

    fig = apply_chart_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

def render_latency_chart(df):
    fig = px.bar(
        df,
        x="Backend",
        y="Latency_ms",
        text="Latency_ms",
        title="Inference Latency by Backend",
        color="Backend",
        color_discrete_sequence=["#6d5dfc", "#2563eb", "#22c55e", "#f59e0b"]
    )
    fig.update_layout(height=310, showlegend=False)
    fig = apply_chart_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

def render_memory_chart(df):
    fig = px.pie(
        df,
        names="Backend",
        values="Memory_MB",
        title="Memory Usage Distribution",
        hole=0.45,
        color_discrete_sequence=["#6d5dfc", "#2563eb", "#22c55e", "#f59e0b"]
    )
    fig.update_layout(height=310)
    fig = apply_chart_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

def render_throughput_chart(df):
    fig = px.line(
        df,
        x="Backend",
        y="Throughput_tokens_sec",
        markers=True,
        title="Throughput Comparison"
    )

    fig.update_traces(
        line=dict(color="#22c55e", width=4),
        marker=dict(size=10, color="#6d5dfc")
    )

    fig.update_layout(height=310)
    fig = apply_chart_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

def render_training_chart():
    data = {
        "Epoch": [1, 2, 3, 4, 5],
        "Training Loss": [2.41, 2.18, 2.01, 1.92, 1.84],
        "Validation Loss": [2.52, 2.31, 2.13, 2.02, 1.91]
    }

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data["Epoch"],
        y=data["Training Loss"],
        mode="lines+markers",
        name="Training Loss",
        line=dict(color="#6d5dfc", width=4)
    ))

    fig.add_trace(go.Scatter(
        x=data["Epoch"],
        y=data["Validation Loss"],
        mode="lines+markers",
        name="Validation Loss",
        line=dict(color="#ef4444", width=4)
    ))

    fig.update_layout(
        title="Training and Validation Loss",
        height=360,
        xaxis_title="Epoch",
        yaxis_title="Loss"
    )

    fig = apply_chart_theme(fig)
    st.plotly_chart(fig, use_container_width=True)