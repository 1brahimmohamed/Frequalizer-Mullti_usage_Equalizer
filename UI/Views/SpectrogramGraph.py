import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import plotly.graph_objects as go


class SpectrogramGraph():
    def __init__(self):
        self.fig = go.Figure()
        self.fig.update_layout(yaxis_title="Spectogram")
        self.fig.update_xaxes(showgrid=False, automargin=True)
        self.fig.update_yaxes(showgrid=False, automargin=True)

        self.fig.update_layout(
            height=180,
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
        
        st.plotly_chart(self.fig)