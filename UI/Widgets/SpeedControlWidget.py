import streamlit as st

class SpeedControlWidget:
    def __init__(self):
        st.slider("Speed Control", 0.5, 2.0, 1.0, 0.1)