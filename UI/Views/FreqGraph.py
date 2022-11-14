import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st
import time
import numpy as np

class FreqGraph:
    def __init__(self, key, isUpdated):
        if isUpdated:
            signalDataFrame = pd.DataFrame({
                't':st.session_state.currentSignal['time'],
                'y':st.session_state.currentSignal['updatedSignal']
            })
        else:
            signalDataFrame = pd.DataFrame({
                't':st.session_state.currentSignal['time'],
                'y':st.session_state.currentSignal['signal']
            }) 


        lines = alt.Chart(signalDataFrame).mark_line().encode(
            alt.X('t', scale=alt.Scale(domain=(0, 0.1))),
            alt.Y('y')

        ).properties(
            width=600,
            height=150
        ).add_selection(
            st.session_state.zoom
        )

        st.session_state['{}'.format(key)] = lines
