import os
import streamlit.components.v1 as components
import streamlit as st
from state_management.state_management import state_management

class SliderWidget:
    def __init__(self, label, value, min, max, key):
        state = state_management()
        _vertical_slider = components.declare_component(
            "vertical_slider",
            path='./UI/Widgets/build',
        )
        slider = _vertical_slider(label = label, value = value, min = min, max = max)
        st.session_state['_{}_'.format(key)] = slider

        if '_{}'.format(key) not in st.session_state:
            st.session_state['_{}'.format(key)] = -1

        if(slider and slider != st.session_state['_{}'.format(key)] and st.session_state.uploadButton):
            st.session_state['_{}'.format(key)] = slider
            state.change_slider_value(int(key[7:]), slider)
            st.experimental_rerun()

        