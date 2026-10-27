from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="HIV安宁疗护沟通训练",
    page_icon="💬",
    layout="wide",
)

st.iframe(
    Path(__file__).with_name("index.html"),
    height="content",
    width="stretch",
    alt="HIV安宁疗护沟通训练：15个合成病例、模拟患者对话、知识问答和NURSE/SHARE参考反馈。",
)
