import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
import yfinance as yf
import os
from math import factorial
from streamlit.components.v1 import html
# Sidebar
with st.sidebar:
    # Información del proyecto
    st.title("Proyecto - AMIB 2026")
    st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)
    st.markdown("""
    *Autores:*
    - Autor 1
    - Autor 2 
    - Autor 3
    - Autor ...
    """)
    # Layouts
    st.header("Escoge el tema de tu interés", divider="red")
    ## Selectbox
    selectbox_1 = st.selectbox(
        "Temas financieros",
        ["Inflación", "IPC","Derivados","Acciones","ETF's"],
        index=1
    )
    st.markdown("---")

# Footer personalizado
html("""
<div style="text-align: center; padding: 20px; margin-top: 30px; background-color: #4A4A4A; color: white; border-radius: 10px;">
    <p> © 2026 Asiación Méxica de Istituciones Bancarias | Finance and Young  </p>
</div>
""")
