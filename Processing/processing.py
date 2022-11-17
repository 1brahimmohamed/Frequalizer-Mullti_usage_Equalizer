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

    def fourier_function(self, signal):
        song = signal['signal']
        sampleRate = signal['sampleRate']

        complex_fft = scipy.fft.rfft(song)
        magnitude = np.abs(complex_fft)
        phase = np.angle(complex_fft)
        frequency = scipy.fft.rfftfreq(len(song), 1 / sampleRate)
        return magnitude, phase, frequency

    # function that uses triangle window to manipulate data, still not done
    def equalizerRange_Triangle(self, signal, slider_ranges, slider_dB):
        magnitude = signal['magnitude']
        newMagnitude = signal['newMagnitude']
        frequency = signal['freq']

        #manipulate mag over a specific range
        slider_dB = int(slider_dB)
        for rng in slider_ranges:
            # adjust magnitude of range in list
            target_freq= list(np.where((frequency>rng[0])&(frequency<rng[1]))[0])
            #generate a triangular window
            triangle_window = 10**((slider_dB)*scipy.signal.windows.triang(len(target_freq)))

            for i, window in zip(target_freq,triangle_window):
                newMagnitude[i] = magnitude[i] * window

        return newMagnitude


    # inverse reconstruction of signal ==> y[frequency]= (magnitude*(e^(phase)))
    def calc_inv_fourier(self, mag, phase):
        New_signal = np.multiply(mag, np.exp(1j * phase))
        inv_fourier_signal = np.real(scipy.fft.irfft(New_signal))
        #inv_fourier_signal = inv_fourier_signal.astype(np.int16) #commented cuz it breaks the function, dunno why
        return inv_fourier_signal