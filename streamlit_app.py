from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="HIV安宁疗护沟通训练",
    page_icon="💬",
    layout="wide",
)

st.set_option("client.toolbarMode", "minimal")
st.markdown(
    """<style>
    header[data-testid="stHeader"] { display: none !important; }
    .stMainBlockContainer { padding: 0; max-width: none; }
    [data-testid="stElementContainer"]:has(> iframe[data-testid="stIFrame"]) {
        height: calc(100dvh - 1rem) !important;
        min-height: 0 !important;
    }
    iframe[data-testid="stIFrame"] { height: 100% !important; }
    </style>""",
    unsafe_allow_html=True,
)

st.iframe(
    Path(__file__).with_name("index.html"),
    height=900,
    width="stretch",
    tab_index=0,
    alt="HIV安宁疗护沟通训练：15个合成病例、模拟患者对话、知识问答和NURSE/SHARE参考反馈。",
)
