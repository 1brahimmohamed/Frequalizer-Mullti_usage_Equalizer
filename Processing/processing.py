import librosa 
import librosa.display as dsp
import numpy as np
import scipy
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt 
from IPython.display import Audio as audioPlayer


class Processing:
    def __init__(self):
        pass

    def read_signal(self, file):
        song, sampleRate = librosa.load(file, offset=1.0 , duration=20.0)
        return song, sampleRate

