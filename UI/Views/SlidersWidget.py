import streamlit as st
from UI.Widgets.SliderWidget import SliderWidget
from Data.SlidersData import slidersData,SlidersColumns


class SlidersWidget:
    def __init__(self, Mode):
        try:
            columnsLst = SlidersColumns[Mode]
            cols = st.columns(columnsLst)

            counter = 0
            if Mode == 0:
                if len(st.session_state.fourierSignal['freq']) != 0:
                    maxFreq = max(st.session_state.fourierSignal['freq'])
                    sliderV = maxFreq/8
                    sliderRanges = ["{}: {}Hz".format(int(sliderV * i), int(sliderV * (i + 1))) for i in range(0, 8)]
                else:
                    sliderRanges = ["0: 2750Hz", "2750: 5500Hz", "5500, 8250Hz", "8250: 11000Hz",
                                    "11000: 13750Hz", "13750: 16500Hz", "16500: 19250Hz", "19250: 22000Hz"]
            resetFlag = True
            for i in range(1, len(columnsLst), 2):
                with cols[i]:
                    sliderLabel = ""
                    if Mode == 0:
                        sliderLabel = sliderRanges[counter]
                    else:
                        sliderLabel = slidersData[Mode][counter]['label']
                    SliderWidget(sliderLabel, 0, -5, 5, "Slider{}{}".format(Mode, str(counter)))
                    
                    if (st.session_state["_Slider{}{}_".format(Mode, str(counter))] != None) \
                        and (st.session_state["_Slider{}{}_".format(Mode, str(counter))] != '0'):
                        resetFlag = False

                    counter+=1


            if resetFlag and st.session_state.sliderState:
                st.session_state.sliderState = False
                st.session_state.currentSignal['updatedSignal'] = st.session_state.currentSignal['signal'] 
                st.session_state.fourierSignal['newMagnitude'] = st.session_state.fourierSignal['magnitude']
                st.experimental_rerun()

        except Exception as e:
            st.error(e)