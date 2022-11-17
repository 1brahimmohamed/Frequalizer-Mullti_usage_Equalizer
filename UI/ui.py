import os

import altair as alt
import streamlit as st
import streamlit_nested_layout
import soundfile as sf

from state_management.state_management import state_management
from UI.Views.FreqGraph import FreqGraph
from UI.Views.SlidersWidget import SlidersWidget
from UI.Views.SpectrogramGraph import SpectrogramGraph
from UI.Widgets.UploadWidget import UploadWidget
from UI.Widgets.SpeedControlWidget import SpeedControlWidget


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

        columns = st.columns([0.4, 2, 0.4, 4, 0.4])

        with columns[1]:
            UploadWidget()
            columns1 = st.columns([0.1, 0.05, 0.07, 0.1])
            with columns1[1]:
                st.button(st.session_state.emotionState, 'startButton', on_click=self.start)
            with columns1[2]:
                st.button('⏹️', 'stopButton', on_click=self.stop)
            nestedCols = st.columns([0.1, 2, 0.1, 2, 0.1])
            with nestedCols[1]:
                st.write('Original Signal')
                st.audio(st.session_state.uploadButton, format="audio/wav", start_time=0)
            with nestedCols[3]:
                st.write('Updated Signal')
                if st.session_state.sliderState and sf.read("./uploads/after.wav"):
                    st.audio("./uploads/after.wav", format="audio/wav", start_time=0)
                else:
                    st.audio(st.session_state.uploadButton, format="audio/wav", start_time=0)

            # SpeedControlWidget()
            modesLst = ['Uniform', 'Vowels', 'Music', 'Bio-medical', 'Tone']
            mode = st.selectbox("Select Mode:", options=modesLst)
            if mode:
                st.session_state.Mode = modesLst.index(mode)


        st.session_state.zoom = alt.selection_interval(bind='scales')
        FreqGraph('pureLinePlot', False)
        FreqGraph('LinePlot', True)

        with columns[3]:
            st.write("---")
            st.session_state['graph'] = st.altair_chart(alt.hconcat(st.session_state['pureLinePlot'], 
                                                                    st.session_state['LinePlot']))
            SpectrogramGraph()

        SlidersWidget(st.session_state.Mode)
                
        if st.session_state.startState == True:
            state.start_signal_drawing()

    def start(self):
        st.session_state.startState = not(st.session_state.startState)
        if st.session_state.startState == True:
            st.session_state.emotionState = '⏸'
        else:
            st.session_state.emotionState = '▶️'
        st.session_state.startTime = st.session_state.counter

    def stop(self):
        st.session_state.startState = False
        st.session_state.startTime = 0

    