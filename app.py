import streamlit as st
import pandas as pd
from data_loader import load_data
from analyzer import analyze
from config import MIN_CONFIDENCE

st.set_page_config(page_title="Analisador de Velas", layout="centered")

st.title("📊 Analisador de Padrão de Velas")

uploaded_file = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df['time'] = pd.to_datetime(df['time'])
    df['hour_min'] = df['time'].dt.strftime('%H:%M')
    df['color'] = df.apply(lambda row: 'green' if row['close'] > row['open'] else 'red', axis=1)

    results = analyze(df, MIN_CONFIDENCE)

    st.subheader("📈 Resultados")

    if results:
        for r in results:
            st.write(f"⏰ {r['time']} → {r['direction']} | {r['confidence']}% | {r['samples']} velas")
    else:
        st.warning("Nenhum padrão forte encontrado.")
