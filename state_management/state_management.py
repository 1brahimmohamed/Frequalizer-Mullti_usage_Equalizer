import streamlit as st
from Processing.processing import Processing
import altair as alt
import time
import numpy as np
import pandas as pd
from Data.SlidersData import slidersData
import scipy
import soundfile
from scipy.misc import electrocardiogram
import pyrubberband as pyrb


class state_management:
    def __init__(self):
        if 'x' not in st.session_state:
            st.session_state.x = None

        if 'Mode' not in st.session_state:
            st.session_state.Mode = 0

        if 'currentSignal' not in st.session_state:
            st.session_state.currentSignal = {
                'signal': [],
                'updatedSignal': [],
                'time': [],
                'sampleRate': 0
            }

        if 'fourierSignal' not in st.session_state:
            st.session_state.fourierSignal = {
                'magnitude': [],
                'newMagnitude': [],
                'phase': [],
                'freq': []
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

        if 'medicalMode' not in st.session_state:
            st.session_state.medicalMode = True

    def save_file(self, file):
        processing = Processing()
        song, sampleRate = processing.read_signal(file)
        t = np.linspace(start=0, num=len(song), stop=(len(song) / sampleRate))

        if (len(t) > len(song)):
            song = song[:len(t)]
        st.session_state.currentSignal = {
            'time': t,
            'signal': song,
            'updatedSignal': song,
            'sampleRate': sampleRate
        }

        self.fourier_transform()

        st.session_state.sliderState = False

    def start_signal_drawing(self):
        timeLst = []
        signalLst = []
        updatedLst = []

        for i in range(0, len(st.session_state.currentSignal['time']), 50):
            timeLst.append(st.session_state.currentSignal['time'][i])
            signalLst.append((st.session_state.currentSignal['signal'][i]))
            updatedLst.append((st.session_state.currentSignal['updatedSignal'][i]))

        signalDataFrame = pd.DataFrame({
            't': timeLst,
            'y': signalLst
        })
        updatedSignalDataFrame = pd.DataFrame({
            't': timeLst,
            'y': updatedLst
        })

        N = signalDataFrame.shape[0]

        burst = 200
        size = burst

        graph = st.session_state.graph

        st.session_state.counter = st.session_state.startTime

        while (st.session_state.counter < N):
            dfStep = signalDataFrame.iloc[st.session_state.counter:st.session_state.counter + size]
            updatedDfStep = updatedSignalDataFrame.iloc[st.session_state.counter:st.session_state.counter + size]
            lines = self.plot_animation(dfStep)

            updatedLines = self.plot_animation(updatedDfStep)

            graph = graph.altair_chart(alt.hconcat(lines, updatedLines))
            time.sleep(0.05)
            st.session_state.counter += 5

    def plot_animation(self, df):
        lines = alt.Chart(df).mark_line().encode(
            alt.X('t'),
            alt.Y('y')
            # alt.Y('y', scale=alt.Scale(domain=(-0.0002, 0.0002)))
        ).properties(
            width=380,
            height=150
        )
        return lines

    def change_slider_value(self, sliderIndex, sliderValue):
        flag = True
        if st.session_state.Mode == 0:
            maxFreq = max(st.session_state.fourierSignal['freq'])
            sliderV = maxFreq / 8
            sliderRanges = [[sliderV * sliderIndex, sliderV * (sliderIndex + 1)]]
        elif st.session_state.Mode == 4:
            st.session_state.currentSignal['updatedSignal'] = pyrb.pitch_shift(st.session_state.currentSignal['signal'], \
                                                                               st.session_state.currentSignal[
                                                                                   'sampleRate'], sliderValue)
            flag = False
        else:
            sliderRanges = slidersData[st.session_state.Mode][sliderIndex]['freqRanges']
        if flag:
            processing = Processing()
            st.session_state.fourierSignal['newMagnitude'] = processing.equalizerRange_Triangle(
                st.session_state.fourierSignal, sliderRanges, sliderValue)

            st.session_state.currentSignal['updatedSignal'] = processing.calc_inv_fourier(
                st.session_state.fourierSignal['newMagnitude'],
                st.session_state.fourierSignal['phase'])
        soundfile.write("./uploads/after.wav", st.session_state.currentSignal['updatedSignal'],
                        st.session_state.currentSignal['sampleRate'])

        st.session_state.sliderState = True

    def change_to_medical_mode(self):
        if st.session_state.medicalMode:
            song = electrocardiogram()
            sampleRate = 360
            time = np.arange(song.size) / sampleRate

            slicedSong = []
            slicedTime = []
            for i in range(len(time)):
                if (time[i] >= 45 and time[i] < 51):
                    slicedSong.append(song[i])
                    slicedTime.append(time[i])
                elif time[i] > 51:
                    break

            st.session_state.currentSignal = {
                'signal': slicedSong,
                'updatedSignal': slicedSong,
                'time': slicedTime,
                'sampleRate': sampleRate
            }
            self.fourier_transform()

            st.session_state.medicalMode = False

    def fourier_transform(self):
        processing = Processing()
        magnitude, phase, frequency = processing.fourier_function(st.session_state.currentSignal)
        st.session_state.fourierSignal = {
            'magnitude': magnitude,
            'newMagnitude': magnitude,
            'phase': phase,
            'freq': frequency
        }
