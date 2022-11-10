import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st
import time
import numpy as np

class FreqGraph:
    def __init__(self, signal, key):
        signalDataFrame = pd.DataFrame({
            't':signal['time'],
            'y':signal['signal']
        })    

        lines = alt.Chart(signalDataFrame).mark_line().encode(
            alt.X('t', scale=alt.Scale(domain=(0, 0.1))),
            alt.Y('y')

        ).properties(
            width=470,
            height=200
        ).add_selection(
            st.session_state.zoom
        )

        st.session_state['{}'.format(key)] = lines
