import streamlit as st
import plotly.graph_objects as go


class FreqGraph:
    def __init__(self):
        self.fig = go.Figure()
        self.fig.update_layout(xaxis_title="time", yaxis_title="Amplitude")
        self.fig.update_xaxes(showgrid=False, automargin=True)
        self.fig.update_yaxes(showgrid=False, automargin=True)

        self.fig.update_layout(
            height=200,
            margin={
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0
            }
        )
        self.fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        # Signal Drawing
        # if (not (st.session_state.currentSignal['signal'].empty)) and (st.session_state.signalView):
        #     self.fig.add_trace(go.Scatter(
        #         x=st.session_state.currentSignal['signal'].iloc[:, 0],
        #         y=st.session_state.currentSignal['signal'].iloc[:, 1],
        #         mode='lines',
        #         name='signal'))

        st.plotly_chart(self.fig, use_container_width=True)