#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dashboard com Streamlit para visualização de dados.
Uso: streamlit run dashboard_dados.py
"""

import streamlit as st
import pandas as pd
import numpy as np
from utils.helpers import setup_logger

st.title("Dashboard Automatizado de Dados")

# Dados mock
df = pd.DataFrame(
    {
        "Vendas": np.random.randn(100).cumsum(),
        "Data": pd.date_range("2024-01-01", periods=100),
    }
)

st.line_chart(df.set_index("Data"))

st.dataframe(df.tail())
st.metric("Média Vendas", df["Vendas"].mean())
