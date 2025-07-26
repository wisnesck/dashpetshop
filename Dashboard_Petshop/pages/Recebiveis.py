import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

df_total = pd.read_excel("Dashboard_Petshop/Database/Recebiveis_Petshop.xlsx")

df_recebiveis = df_total[["Nome do Cliente", "Data de compra", "Vencimento", "Valor"]]

lista_client = df_recebiveis["Nome do Cliente"].unique()
clientes_mostrar = st.sidebar.selectbox("📌 Selecione o cliente", lista_client)

# Aplica o filtro
df_filtrado = df_recebiveis[df_recebiveis["Nome do Cliente"] == clientes_mostrar]

# Mostra o resultado
st.dataframe(df_filtrado)

valor_total = df_filtrado["Valor"].sum()

# Exibe o resultado abaixo da tabela
st.markdown(f"### 💰 Total a receber do cliente: R$ {valor_total:,.2f}")




