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
    
        lines = alt.Chart(signalDataFrame.iloc[st.session_state.startTime: 
                                                st.session_state.startTime + 500,:]).mark_line().encode(
            x='t',
            y='y'
        ).properties(
            width=480,
            height=200
        )
        st.session_state['{}'.format(key)] = st.altair_chart(lines)