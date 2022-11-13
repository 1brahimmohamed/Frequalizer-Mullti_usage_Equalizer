import os
import streamlit.components.v1 as components


class PlayBtnWidget:
    def __init__(self):
        play_pause_btn = components.declare_component(
            "vertical_slider",
            path='./UI/Widgets/PlayBtnBuild',
        )
        component_value = play_pause_btn()
