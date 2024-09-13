
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

import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data

# Load dataset
df = pd.read_csv("./dados/Pasta1.csv", sep=';')

# Sidebar with month selection
meses = df["MES"].value_counts().index
mes = st.sidebar.selectbox("MES", meses)

# Simulated chart data
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# Render HTML for header
st.markdown("""
    <header class="navbar" style="padding: 20px 0; background-color: #f8f8f8; text-align: center;">
        <div class="logo">
            <img src="assets/img/logo.png" alt="Logo">
        </div>
        <h1>Estatística - Autoridade Portuária de Santos</h1>
    </header>
""", unsafe_allow_html=True)

# Main section with charts
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Row 1: Monthly Data
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2>Mensal - Volume Mensal</h2>", unsafe_allow_html=True)
    st.bar_chart(chart_data)

with col2:
    st.markdown("""
    <h2>Julho/24</h2>
    <p>Volume: 16,4 Mi</p>
    <p>Variação: 6,8%</p>
    """, unsafe_allow_html=True)

# Row 2: Carga Data
st.markdown("<h2>Perfil de Carga - Mês</h2>", unsafe_allow_html=True)
st.bar_chart(chart_data)

# Row 3: Accumulated Data
col3, col4 = st.columns(2)

with col3:
    st.markdown("<h2>Acumulado no Ano</h2>", unsafe_allow_html=True)
    st.bar_chart(chart_data)

with col4:
    st.markdown("""
    <h2>Até Julho/24</h2>
    <p>Acumulado: 105,6 Mi</p>
    <p>Variação: 9,5%</p>
    """, unsafe_allow_html=True)

# Row 4: Year Data
st.markdown("<h2>Perfil de Carga - Ano</h2>", unsafe_allow_html=True)
st.bar_chart(chart_data)

# End the container
st.markdown("</div>", unsafe_allow_html=True)
