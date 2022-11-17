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

        startX = 0
        if not signalDataFrame.empty:
            startX = st.session_state.currentSignal['time'][st.session_state.counter]
        lines = alt.Chart(signalDataFrame).mark_line().encode(
            alt.X('t', scale=alt.Scale(domain=(startX, startX + 1))),
            alt.Y('y')

        ).properties(
            width=380,
            height=150
        ).add_selection(
            st.session_state.zoom
        )

        st.session_state['{}'.format(key)] = lines
