import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_produtos = pd.read_excel("Dashboard_Petshop/Database/Produtos.xlsx")

produtos = df_produtos[["nome" , "categoria", "estoque", "preco unitario", "quantidade_vendida"]]

preco_max = produtos["preco unitario"].max()
preco_min = produtos["preco unitario"].min()

faixa = st.sidebar.slider(
    "Faixa de Preço",
    min_value=float(preco_min),
    max_value=float(preco_max),
    value=(float(preco_min), float(preco_max)),
    step=0.5
)

# Agora sim, filtrando pelo intervalo selecionado
faixa_preco = produtos[
    (produtos["preco unitario"] >= faixa[0]) &
    (produtos["preco unitario"] <= faixa[1])
]

st.dataframe(faixa_preco)

fig1 = px.bar(faixa_preco["preco unitario"])
fig2 = px.histogram(faixa_preco["quantidade_vendida"])

fig1
fig2
