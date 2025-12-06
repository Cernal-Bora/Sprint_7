import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Vehicles Project - Cuadro de Mandos")

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", title="Distribución de odometer")
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre odometer y price')
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Kilómetros recorridos")
    st.plotly_chart(fig, use_container_width=True)