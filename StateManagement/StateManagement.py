import streamlit as st

class StateManagement:
    def __init__(self):
        if 'signal' not in st.session_state:
            st.session_state.signal = 0