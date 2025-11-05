# app resultado de ações
import streamlit as st
import yfinance as yf
import pandas as pd


@st.cache_data

def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotaçoes_acao = dados_acao.history(period='1d', start='2000-01-01', end='2024-07-01')
    cotacoes_acao = cotacoes_acao[["Close"]]
    return cotacoes_acao
    


dados  = carregar_dados("ITUB4.SA")
print(dados)
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações do Itaú (ITUB4) ao longo dos anos
""")

st.line_chart(dados)
 
st.write("""
# Fim do app
""")



