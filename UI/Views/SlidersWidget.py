import streamlit as st
from UI.Widgets.SliderWidget import SliderWidget
from Data.SlidersData import slidersData
# from StateManagement.StateManagement import StateManagement


class SlidersWidget:
    def __init__(self):
        # State = StateManagement()

        try:
            columnsLst = []
            for i in range(len(slidersData[st.session_state.Mode])):
                columnsLst.append(0.05)
                columnsLst.append(0.4)
            columnsLst.append(0.2)

            cols = st.columns(columnsLst)

            counter = 0
            for i in range(1, len(columnsLst), 2):
                with cols[i]:
                    lst = slidersData[st.session_state.Mode][counter]['sliderRange']
                    SliderWidget(lst[0], lst[1], lst[2], "Slider{}".format(str(counter)))
                    counter+=1
                
        except Exception as e:
            st.error(e)

    def change_upload_value(self):
        pass