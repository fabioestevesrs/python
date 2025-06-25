import streamlit as st
import pandas as pd
import plotly.express as px

# terminal:streamlit run main.py

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

# conversão de object para datetime
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

# criando um filtro baseado na caixa de seleção criado com mês/ano, e comparando com a coluna Month
df_filtered = df[df["Month"] == month]
# df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total",
                  title="Faturamento por dia", color="City")
col1.plotly_chart(fig_date)

fig_product = px.bar(df_filtered, x="Date", y="Product line",
                     title="Faturamento por tipo de produto", color="City", orientation="h")
col2.plotly_chart(fig_product)
