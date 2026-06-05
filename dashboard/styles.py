import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    :root {
        --bg: #f8fbff;
        --card: #ffffff;
        --text: #0f172a;
        --muted: #64748b;
        --border: #e2e8f0;
        --primary: #6d5dfc;
        --green: #16a34a;
        --blue: #2563eb;
        --orange: #f59e0b;
        --red: #ef4444;
    }

    .stApp {
        background: linear-gradient(135deg, #f8fbff, #ffffff);
        color: var(--text);
    }

    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    section[data-testid="stSidebar"] * {
        color: #111827 !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }

    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: #0f172a;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 900;
        color: #6d5dfc;
        margin-bottom: 4px;
    }

    .hero-subtitle {
        font-size: 15px;
        color: #475569;
        margin-bottom: 22px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 800;
        margin: 18px 0 14px 0;
        color: #0f172a;
    }

    .kpi-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 22px;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
        min-height: 120px;
    }

    .kpi-label {
        font-size: 13px;
        color: #475569;
        font-weight: 700;
    }

    .kpi-value {
        font-size: 26px;
        color: #0f172a;
        font-weight: 900;
        margin-top: 6px;
    }

    .kpi-note {
        font-size: 12px;
        color: #64748b;
        margin-top: 4px;
    }

    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    }

    .status-box {
        background: #ecfdf5;
        color: #047857;
        border: 1px solid #bbf7d0;
        padding: 16px;
        border-radius: 14px;
        font-weight: 700;
        margin-top: 15px;
    }

    .activity-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
        min-height: 260px;
    }

    .activity-row {
        display: flex;
        gap: 12px;
        align-items: flex-start;
        margin-bottom: 18px;
    }

    .activity-dot {
        width: 22px;
        height: 22px;
        border-radius: 50%;
        background: #22c55e;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        font-weight: 900;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 12px;
        padding: 20px;
        margin-top: 20px;
    }

    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    }

    div[data-testid="stMetricLabel"] p {
        color: #334155 !important;
        font-weight: 700;
    }

    div[data-testid="stMetricValue"] {
        color: #0f172a !important;
    }

    div[data-testid="stMetricDelta"] {
        color: #16a34a !important;
    }

    textarea, input, select {
        background: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
    }

    .stButton button {
        background: linear-gradient(90deg, #6d5dfc, #7c3aed);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        padding: 0.6rem 1rem;
    }

    .stButton button:hover {
        background: linear-gradient(90deg, #5b4df5, #6d28d9);
        color: white;
    }

    [data-testid="stDataFrame"] {
        background: white;
        border-radius: 14px;
    }

    .stAlert {
        background: #eff6ff;
        color: #1e3a8a;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)