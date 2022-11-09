import streamlit as st
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from Processing.processing import Processing
import soundfile as sf
import librosa 
import altair as alt
import time
import numpy as np 
import pandas as pd

class state_management:
    def __init__(self):
        if 'Mode' not in st.session_state:
            st.session_state.Mode = 0
        
        if 'currentSignal' not in st.session_state:
            st.session_state.currentSignal = {
                'signal':[],
                'time':[],
                'sampleRate':0
            }

        if 'startState' not in st.session_state:
            st.session_state.startState = False

        if 'startTime' not in st.session_state:
            st.session_state.startTime = 0

        if 'counter' not in st.session_state:
            st.session_state.counter = 0


    def save_file(self, file):       
        processing = Processing()
        song, sampleRate = processing.read_signal(file)
        t = np.linspace(start=0, num=len(song), stop=(len(song)/sampleRate))
        st.session_state.currentSignal = {
            'time':t,
            'signal':song,
            'sampleRate':sampleRate
        }


    def start_signal_drawing(self):
        signalDataFrame = pd.DataFrame({
            't':st.session_state.currentSignal['time'],
            'y':st.session_state.currentSignal['signal']
        })
        
        N = signalDataFrame.shape[0] 
        burst = 500
        size = burst
        pureLinePlot = st.session_state.pureLinePlot
        LinePlot = st.session_state.LinePlot

        st.session_state.counter = st.session_state.startTime
        while(st.session_state.counter < N):
            step_df = signalDataFrame.iloc[st.session_state.counter:st.session_state.counter + size]
            lines = self.plot_animation(step_df)
            #---------------------------------------
            pureLinePlot = pureLinePlot.altair_chart(lines)
            LinePlot = LinePlot.altair_chart(lines)
            #---------------------------------------
            time.sleep(0.001)
            st.session_state.counter += 1


    def plot_animation(self, df):
        lines = alt.Chart(df).mark_line().encode(
            x='t',
            y='y',
        ).properties(
        width=480,
        height=200
        ) 
        return lines
