import streamlit as st
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from Processing.processing import Processing
import soundfile as sf
import librosa 


class state_management:
    def __init__(self):
        if 'Mode' not in st.session_state:
            st.session_state.Mode = 0
        
        if 'currentSignal' not in st.session_state:
            st.session_state.currentSignal = {
                'signal':[],
                'sampleRate':0
            }


    def save_file(self, file):       
        processing = Processing()
        song, sampleRate = processing.read_signal(file)
        st.session_state.currentSignal = {
            'signal':song,
            'sampleRate':sampleRate
        }