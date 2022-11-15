import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from state_management.state_management import state_management
import librosa 
import librosa.display as dsp



class SpectrogramGraph():
    def __init__(self):
        State = state_management()

        fig, ax = plt.subplots(1, 2, figsize=(12,2.5))
        if len(st.session_state.currentSignal['signal']) != 0:

            signal = np.array(st.session_state.currentSignal['signal'])
            updatedSignal = np.array(st.session_state.currentSignal['updatedSignal'])

            sampleRate = st.session_state.currentSignal['sampleRate']

            d = librosa.stft(signal)
            dUpdated = librosa.stft(updatedSignal)
            
            D = librosa.amplitude_to_db(np.abs(d),ref=np.max)
            DUpdated = librosa.amplitude_to_db(np.abs(dUpdated),ref=np.max)


            img = dsp.specshow(D, y_axis='linear', x_axis='s',sr=sampleRate,ax=ax[0])
            imgUpdated = dsp.specshow(DUpdated, y_axis='linear', x_axis='s',sr=sampleRate,ax=ax[1])

            dsp.specshow(D,y_axis='log',x_axis='s',sr=sampleRate,ax=ax[0])
            dsp.specshow(DUpdated,y_axis='log',x_axis='s',sr=sampleRate,ax=ax[1])

            ax[0].set(title='Original Signal spectrogram')
            ax[1].set(title='Updated Signal spectrogram')

            fig.colorbar(img, ax=ax[0], format='%+2.f dB')
            fig.colorbar(imgUpdated, ax=ax[1], format='%+2.f dB')
            plt.tight_layout()
            
        st.pyplot(fig)