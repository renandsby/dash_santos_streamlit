
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_ace import st_ace
from vega_datasets import data

# df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')


df = pd.read_csv("./dados/Pasta1.csv",sep=';')
meses = df["MES"].value_counts().index
mes = st.sidebar.selectbox("MES",meses)
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

source = data.barley()

col1, col2, col3 = st.columns([0.3, 0.3,0.3])
col1.bar_chart(source, x="year", y="yield", color="site", stack=False)
col2.area_chart(chart_data)
col3.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)

col4, col5, col6 = st.columns(3)
col4.bar_chart(source, x="year", y="yield", color="site", stack=False)
col5.bar_chart(chart_data)
col6.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)
