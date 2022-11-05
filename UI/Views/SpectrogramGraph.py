import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class SpectrogramGraph():
    def __init__(self):
        fig = Figure()
        axes = fig.add_subplot(111)

        for spine in ['right', 'top', 'left', 'bottom']:
            axes.spines[spine].set_color('gray')

        fig.tight_layout()
        # axes.axis('off')

        # Plot the signal

        cmap = plt.get_cmap('inferno')
        
        st.pyplot(fig)