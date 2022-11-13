import os
import streamlit.components.v1 as components


class SliderWidget:
    def __init__(self, value, min, max, key):
        _vertical_slider = components.declare_component(
            "vertical_slider",
            path='./UI/Widgets/SliderBuild',
        )
        _vertical_slider(value=value, min=min, max=max, key=key)