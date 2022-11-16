import streamlit as st
from Processing.processing import Processing
import altair as alt
import time
import numpy as np 
import pandas as pd
from Data.SlidersData import slidersData
import scipy


class state_management:
    def __init__(self):
        if 'x' not in st.session_state:
            st.session_state.x = None

        if 'Mode' not in st.session_state:
            st.session_state.Mode = 0
        
        if 'currentSignal' not in st.session_state:
            st.session_state.currentSignal = {
                'signal':[],
                'updatedSignal':[],
                'time':[],
                'sampleRate':0
            }

        if 'fourierSignal' not in st.session_state:
            st.session_state.fourierSignal = {
                'magnitude':[],
                'newMagnitude':[],
                'phase':[],
                'freq':[]
            }


        if 'startState' not in st.session_state:
            st.session_state.startState = False

        if 'emotionState' not in st.session_state:
            st.session_state.emotionState = '▶'

        if 'startTime' not in st.session_state:
            st.session_state.startTime = 0

        if 'counter' not in st.session_state:
            st.session_state.counter = 0

        if 'sliderState' not in st.session_state:
            st.session_state.sliderState = False


    def save_file(self, file):       
        processing = Processing()
        song, sampleRate = processing.read_signal(file)
        t = np.linspace(start=0, num=len(song), stop=(len(song)/sampleRate))
        st.session_state.currentSignal = {
            'time':t,
            'signal':song,
            'updatedSignal':song,
            'sampleRate':sampleRate
        }
        magnitude, phase, frequency = processing.fourier_function(st.session_state.currentSignal)
        st.session_state.fourierSignal = {
                'magnitude':magnitude,
                'newMagnitude':magnitude,
                'phase':phase,
                'freq':frequency
        }



    def start_signal_drawing(self):
        signalDataFrame = pd.DataFrame({
            't':st.session_state.currentSignal['time'],
            'y':st.session_state.currentSignal['signal']
        })
        updatedSignalDataFrame = pd.DataFrame({
            't':st.session_state.currentSignal['time'],
            'y':st.session_state.currentSignal['updatedSignal']
        })
        
        N = signalDataFrame.shape[0]
        burst = 2000
        size = burst

        graph = st.session_state.graph

        st.session_state.counter = st.session_state.startTime
        while(st.session_state.counter < N):
            dfStep = signalDataFrame.iloc[st.session_state.counter:st.session_state.counter + size]
            updatedDfStep = updatedSignalDataFrame.iloc[st.session_state.counter:st.session_state.counter + size]
            lines = self.plot_animation(dfStep)
            updatedLines = self.plot_animation(updatedDfStep)
            #---------------------------------------
            graph = graph.altair_chart(alt.hconcat(lines, updatedLines))
            # pureLinePlot = pureLinePlot.altair_chart(lines)
            # LinePlot = LinePlot.altair_chart(lines)
            #---------------------------------------
            time.sleep(0.001)
            st.session_state.counter += 1


    def plot_animation(self, df):
        lines = alt.Chart(df).mark_line().encode(
            x='t',
            y='y',
        ).properties(
            width=380,
            height=150
        ) 
        return lines

    def change_slider_value(self, sliderIndex, sliderValue):
        if st.session_state.Mode == 0:
            maxFreq = max(st.session_state.fourierSignal['freq'])
            sliderV = maxFreq/8
            sliderRanges = [[sliderV * sliderIndex, sliderV * (sliderIndex + 1)]]
        else:
            sliderRanges = slidersData[st.session_state.Mode][sliderIndex]['freqRanges']
        processing = Processing()
        st.session_state.fourierSignal['newMagnitude'] = processing.equalizerRange_Triangle(
                                st.session_state.fourierSignal, sliderRanges, sliderValue)

        st.session_state.currentSignal['updatedSignal'] = processing.calc_inv_fourier(st.session_state.fourierSignal['newMagnitude'],
                                st.session_state.fourierSignal['phase'])

        scipy.io.wavfile.write("./uploads/after.wav", st.session_state.currentSignal['sampleRate'],
                                                    st.session_state.currentSignal['updatedSignal'])
        st.session_state.sliderState = True