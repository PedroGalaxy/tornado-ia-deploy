import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("modelo_rf.pkl")

st.title("Predição de Magnitude de Tornado (IA)")

st.write("Insira os valores abaixo:")

yr = st.number_input("Ano", min_value=1950, max_value=2025, value=2021)
mo = st.number_input("Mês", min_value=1, max_value=12, value=5)
slat = st.number_input("Latitude inicial", value=35.0)
slon = st.number_input("Longitude inicial", value=-90.0)
length = st.number_input("Comprimento (LEN)", value=10.0)
width = st.number_input("Largura (WID)", value=100.0)

btn = st.button("Prever Magnitude")

if btn:
    x = np.array([[yr, mo, slat, slon, length, width]])
    pred = model.predict(x)[0]
    st.success(f"Magnitude prevista: {pred:.2f}")
