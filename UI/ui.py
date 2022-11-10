import streamlit as st
from state_management.state_management import state_management
from UI.Widgets.UploadWidget import UploadWidget
from UI.Views.SlidersWidget import SlidersWidget
from UI.Views.FreqGraph import FreqGraph
from UI.Views.SpectrogramGraph import SpectrogramGraph
import os



class AppUi:
    def __init__(self):
        state = state_management()
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


        columns2 = st.columns([0.1, 1.5, 0.1, 2, 0.01, 2, 0.2])
        with columns2[1]:
            UploadWidget()
            st.button('Play/Pause', 'startButton', on_click=self.start)
            st.button('Stop Button', 'stopButton', on_click=self.stop)

        with columns2[3]:
            FreqGraph(st.session_state.currentSignal, 'pureLinePlot')
            SpectrogramGraph()
        
        with columns2[5]:
            FreqGraph(st.session_state.currentSignal, 'LinePlot')
            SpectrogramGraph()

        SlidersWidget()
        if st.session_state.startState == True:
            state.start_signal_drawing()

    def start(self):
        st.session_state.startState = not(st.session_state.startState)
        st.session_state.startTime = st.session_state.counter

    def stop(self):
        st.session_state.startState = False
        st.session_state.startTime = 0

    