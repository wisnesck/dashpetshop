import pandas as pd
import streamlit as st
import plotly as px


# Configuração da página
st.set_page_config(page_title="Resumo por Cliente", layout="wide")

# Título da página
st.title("📋 Resumo por Cliente")

# Leitura da planilha
df_total = pd.read_excel("Dashboard_Petshop/Database/Recebiveis_Petshop.xlsx")

# Seleciona colunas relevantes
df_recebiveis = df_total[["Nome do Cliente", "Data de compra", "Valor"]]

# Converte datas
df_recebiveis["Data de compra"] = pd.to_datetime(df_recebiveis["Data de compra"])

# Geração da tabela resumo
resumo = df_recebiveis.groupby("Nome do Cliente").agg({
    "Data de compra": lambda x: x.min().year,
    "Valor": "sum"
}).reset_index()

# Renomeia colunas
resumo.columns = ["Cliente", "Ano da 1ª compra", "Total a receber (R$)"]

# Exibe o dataframe
st.dataframe(resumo.sort_values(by="Total a receber (R$)", ascending=False), use_container_width=True)
