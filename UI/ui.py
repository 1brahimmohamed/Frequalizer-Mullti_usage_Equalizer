import streamlit as st
# from StateManagement.StateManagement import StateManagement
from UI.Widgets.UploadWidget import UploadWidget
from UI.Widgets.SlidersWidget import SlidersWidget
from UI.Views.FreqGraph import FreqGraph
from UI.Views.SpectrogramGraph import SpectrogramGraph

import os

class AppUi:
    def __init__(self):
        # state = StateManagement()
        # config
        st.set_page_config(page_title='Frequalizer')

        # styling injection
        with open(os.path.join(os.path.dirname(__file__), '../Styles/style.css')) as source:
            style = source.read()
        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        columns1 = st.columns([0.1, 2, 0.1])
        with columns1[1]:
            UploadWidget()

        columns2 = st.columns([0.1, 2, 0.05, 2, 0.2])
        with columns2[1]:
            FreqGraph()
            SpectrogramGraph()
        
        with columns2[3]:
            FreqGraph()
            SpectrogramGraph()

        SlidersWidget()
