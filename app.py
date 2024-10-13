import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o dataset
df = pd.read_csv('vehicles.csv')

# Título do aplicativo
st.header('Análise de Anúncios de Carros')

# Botão para gerar um histograma
hist_button = st.button('Criar histograma') # criar um botão
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(df, x="odometer", nbins=50)
    st.plotly_chart(fig, use_container_width=True)

# Botão para gerar um gráfico de dispersão
disp_button = st.button('Criar Gráfico de Dispersão (Preço vs. Quilometragem)'):
if disp_button:
    st.write('Criando um Gráfico de Dispersão (Preço vs. Quilometragem)')
    fig = px.scatter(df, x='odometer', y='price', title='Preço vs. Quilometragem')
    st.plotly_chart(fig, use_container_width=True)
