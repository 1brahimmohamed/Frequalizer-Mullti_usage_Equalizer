import streamlit as st
# from StateManagement.StateManagement import StateManagement


class SlidersWidget:
    def __init__(self):
        # State = StateManagement()

        try:
            with st.container():
                st.write("---")
                st.slider("freq", key="test1")
                st.slider("freq", key="test2")
                st.write("---")

        except Exception as e:
            st.error(e)

    def change_upload_value(self):
        pass