import streamlit as st

class state_management:
    def __init__(self):
        if 'Mode' not in st.session_state:
            st.session_state.Mode = 0
