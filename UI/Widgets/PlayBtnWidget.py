import os
import streamlit.components.v1 as components
import streamlit as st

class PlayBtnWidget:
    def __init__(self):
        play_pause_btn = components.declare_component(
            "vertical_slider",
            path='./UI/Widgets/PlayBtnBuild',
        )
        component_value = play_pause_btn()
        if component_value:
            self.start()

    def start(self):
        st.session_state.startState = not(st.session_state.startState)
        st.session_state.startTime = st.session_state.counter

