import streamlit as st
from UI.Widgets.SliderWidget import SliderWidget
# from StateManagement.StateManagement import StateManagement


class SlidersWidget:
    def __init__(self):
        # State = StateManagement()

        try:
            cols = st.columns([0.1, 2, 0.1, 2, 0.1, 2, 0.1, 2, 0.1])
            with cols[1]:
                SliderWidget(10, 0, 100, "1")

            with cols[3]:
                SliderWidget(10, 0, 100, "2")

            with cols[5]:
                SliderWidget(10, 0, 100, "3")

            with cols[7]:
                SliderWidget(10, 0, 100, "4")
                
        except Exception as e:
            st.error(e)

    def change_upload_value(self):
        pass