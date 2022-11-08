import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from state_management.state_management import state_management
import librosa 
import librosa.display as dsp



class SpectrogramGraph():
    def __init__(self):
        State = state_management()

        fig, ax = plt.subplots(figsize=(8, 4))
        if len(st.session_state.currentSignal['signal']) != 0:
            signal = np.array(st.session_state.currentSignal['signal'])
            sampleRate = st.session_state.currentSignal['sampleRate']
            y_percussive = librosa.effects.percussive(signal, margin=5)
            d = librosa.stft(y_percussive)
            D = librosa.amplitude_to_db(np.abs(d),ref=np.max)

            fig,ax = plt.subplots(2,1,sharex=True,figsize=(10,10))

            img = dsp.specshow(D, y_axis='linear', x_axis='s',sr=sampleRate,ax=ax[0])

            ax[0].set(title='Linear frequency power spectrogram')
            ax[0].label_outer()
            dsp.specshow(D,y_axis='log',x_axis='s',sr=sampleRate,ax=ax[1])
            ax[1].set(title='Log frequency power spectrogram')
            ax[1].label_outer()
            fig.colorbar(img, ax=ax, format='%+2.f dB')

        st.pyplot(fig)