import streamlit as st
from UI.Widgets.SliderWidget import SliderWidget
from Data.SlidersData import slidersData


class SlidersWidget:
    def __init__(self):
        # try:
            columnsLst = []
            for i in range(len(slidersData[st.session_state.Mode])):
                columnsLst.append(0.05)
                columnsLst.append(0.4)
            columnsLst.append(0.2)

            cols = st.columns(columnsLst)

            counter = 0
            for i in range(1, len(columnsLst), 2):
                with cols[i]:
                    # lst = slidersData[st.session_state.Mode][counter]['sliderRange']
                    SliderWidget(0, -5, 5, "Slider{}".format(str(counter)))
                    counter+=1
                
        # except Exception as e:
        #     st.error(e)

    def change_upload_value(self):
        pass