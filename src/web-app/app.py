import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine


DATABASE_URL = "oracle+oracledb://my_user:my_password@localhost:1521/?service_name=my_database"
engine = create_engine(DATABASE_URL)


st.title("Sistema de Irrigação Inteligente")
st.write("Monitoramento e previsão da necessidade de irrigação utilizando dados de sensores e meteorológicos.")


@st.cache_data
def load_data():
    query = 'SELECT * FROM "NutrientHistory" where ROWNUM <= 100'
    df = pd.read_sql(query, con=engine)
    return df

@st.cache_data
def load_weather_data():
    query_weather = """
    SELECT
        temperature AS weather_temperature,
        humidity AS weather_humidity,
        wind_speed,
        pressure,
        date_register
    FROM
        "WeatherHistoricalData"
    """
    weather_df = pd.read_sql(query_weather, con=engine)
    return weather_df


@st.cache_resource
def load_model():
    return joblib.load("../ml_models/model_rf.pkl")

model = load_model()


scaler = joblib.load("../ml_models/scaler.pkl")


menu = st.sidebar.selectbox(
    "Escolha a seção",
    ["Dados do Sensor", "Dados Meteorológicos", "Fazer Previsão", "Gráficos"]
)


if menu == "Dados do Sensor":
    st.subheader("Dados do Sensor ESP32")
    data = load_data()
    st.dataframe(data)


elif menu == "Dados Meteorológicos":
    st.subheader("Dados Meteorológicos")
    weather_data = load_weather_data()
    st.dataframe(weather_data)


elif menu == "Fazer Previsão":
    st.subheader("Fazer Previsão")
    st.write("Insira os dados para realizar uma previsão de irrigação:")

    
    temperature = st.number_input("Temperatura (°C)", value=25.0, step=0.1)
    humidity = st.number_input("Umidade (%)", value=30.0, step=1.0)
    ph = st.number_input("pH", value=7.0, step=0.1)
    weather_temperature = st.number_input("Temperatura Meteorológica (°C)", value=22.0, step=0.1)
    weather_humidity = st.number_input("Umidade Meteorológica (%)", value=10.0, step=1.0)
    wind_speed = st.number_input("Velocidade do Vento (km/h)", value=10.0, step=0.1)
    pressure = st.number_input("Pressão Atmosférica (mbar)", value=1013.0, step=0.1)

    if st.button("Prever"):
        input_data = pd.DataFrame([[temperature, humidity, ph, weather_temperature, weather_humidity, wind_speed, pressure]],
                                  columns=["temperature", "humidity", "ph", "weather_temperature", "weather_humidity", "wind_speed", "pressure"])
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)
        irrigation_status = "Necessário" if prediction[0] == 1 else "Não Necessário"
        st.write(f"Irrigação: **{irrigation_status}**")


elif menu == "Gráficos":
    st.subheader("Gráficos Interativos")
    st.write("Visualize os dados de sensores e meteorológicos em tempo real.")

    data = load_data()
    weather_data = load_weather_data()

    
    st.line_chart(data[['temperature', 'humidity']])

    
    st.scatter_chart(data, x='temperature', y='humidity')

    data.groupby('timestamp')['temperature'].mean()

    st.area_chart(data.groupby('timestamp')['humidity'].mean())
