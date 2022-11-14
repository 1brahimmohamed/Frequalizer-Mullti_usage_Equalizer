import os
import streamlit.components.v1 as components
import streamlit as st

class StopBtnWidget:
    def __init__(self):
        stop_pause_btn = components.declare_component(
            "stop_button",
            path='./UI/Widgets/StopBtnBuild',
        )
        component_value = stop_pause_btn()
        if component_value:
            self.stop()

    def stop(self):
        st.session_state.startState = False
        st.session_state.startTime = 0
