import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o dataset
df = pd.read_csv('vehicles_us.csv')

# Título do aplicativo
st.header('Análise de Anúncios de Carros')

# Botão para gerar um histograma
if st.button('Mostrar Histograma de Preços'):
    fig = px.histogram(df, x='price', nbins=50, title='Distribuição de Preços')
    st.plotly_chart(fig)

# Botão para gerar um gráfico de dispersão
if st.button('Mostrar Gráfico de Dispersão (Preço vs. Quilometragem)'):
    fig = px.scatter(df, x='odometer', y='price', title='Preço vs. Quilometragem')
    st.plotly_chart(fig)
