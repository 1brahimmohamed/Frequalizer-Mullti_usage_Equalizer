import os
import streamlit.components.v1 as components


class StopBtnWidget:
    def __init__(self):
        stop_pause_btn = components.declare_component(
            "stop_button",
            path='./UI/Widgets/StopBtnBuild',
        )
        component_value = stop_pause_btn()
