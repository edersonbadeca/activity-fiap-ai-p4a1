import csv
import random

from dotenv import load_dotenv

from src.services import insert_nutrient_history, import_weather_historical_data

# Load environment variables from .env file
load_dotenv()

import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")

if (DATABASE_URL is None):
    raise Exception("DATABASE_URL environment variable not set")

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def insert_producers():
    session = Session()
    session.execute(text("""
        INSERT INTO "Producers" (name, location) VALUES ('João da Silva', 'São Paulo'), ('Maria Oliveira', 'Rio de Janeiro'), ('José Santos', 'Minas Gerais');
    """))
    session.commit()
    session.close()
    print("Producers inserted successfully")


def insert_crops():
    session = Session()
    session.execute(text("""
        INSERT INTO "Crops" (name, type, id_producer) VALUES ('Rice', 'Grain', 1)
    """))
    session.commit()
    session.close()
    print("Crops inserted successfully")


def insert_sensors():
    session = Session()
    session.execute(text("""
        INSERT INTO "Sensors" (sensor_type, id_crop) VALUES ('humidity', 1)
    """))
    session.commit()
    session.close()
    print("Sensors inserted successfully")


def insert_sensor_readings():
    session = Session()
    session.execute(text("""
INSERT INTO "SensorReadings" (id_sensor, reading_value, reading_date) 
VALUES 
(1, 55.2, TO_DATE('2024-11-06 06:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 56.8, TO_DATE('2024-11-06 09:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.3, TO_DATE('2024-11-06 11:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 52.1, TO_DATE('2024-11-06 14:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 53.9, TO_DATE('2024-11-06 16:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 51.5, TO_DATE('2024-11-06 19:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 58.4, TO_DATE('2024-11-07 08:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 57.0, TO_DATE('2024-11-07 10:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 55.7, TO_DATE('2024-11-07 13:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 49.8, TO_DATE('2024-11-07 15:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 52.6, TO_DATE('2024-11-07 18:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 53.1, TO_DATE('2024-11-08 07:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 50.3, TO_DATE('2024-11-08 10:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.9, TO_DATE('2024-11-08 12:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 51.4, TO_DATE('2024-11-08 15:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 55.8, TO_DATE('2024-11-08 18:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.7, TO_DATE('2024-11-09 07:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 53.5, TO_DATE('2024-11-09 09:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 56.2, TO_DATE('2024-11-09 12:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 52.8, TO_DATE('2024-11-09 14:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 51.9, TO_DATE('2024-11-09 16:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 50.1, TO_DATE('2024-11-09 19:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 52.7, TO_DATE('2024-11-10 06:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.0, TO_DATE('2024-11-10 08:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 55.3, TO_DATE('2024-11-10 11:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 53.8, TO_DATE('2024-11-10 13:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 49.7, TO_DATE('2024-11-10 16:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 52.4, TO_DATE('2024-11-10 18:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 56.9, TO_DATE('2024-11-11 08:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 55.1, TO_DATE('2024-11-11 10:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.4, TO_DATE('2024-11-11 13:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 50.9, TO_DATE('2024-11-11 15:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 53.2, TO_DATE('2024-11-11 17:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.5, TO_DATE('2024-11-12 06:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 55.0, TO_DATE('2024-11-12 09:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 57.6, TO_DATE('2024-11-12 11:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 52.3, TO_DATE('2024-11-12 14:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 50.5, TO_DATE('2024-11-12 16:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 51.7, TO_DATE('2024-11-12 19:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 56.5, TO_DATE('2024-11-13 07:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 58.9, TO_DATE('2024-11-13 09:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.6, TO_DATE('2024-11-13 11:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 50.3, TO_DATE('2024-11-13 13:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 53.5, TO_DATE('2024-11-13 16:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 50.0, TO_DATE('2024-11-13 18:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 55.8, TO_DATE('2024-11-14 08:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.0, TO_DATE('2024-11-14 10:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 53.6, TO_DATE('2024-11-14 13:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 51.4, TO_DATE('2024-11-14 15:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 52.9, TO_DATE('2024-11-14 18:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.2, TO_DATE('2024-11-15 07:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 55.5, TO_DATE('2024-11-15 09:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 56.7, TO_DATE('2024-11-15 11:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 50.6, TO_DATE('2024-11-15 14:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 53.9, TO_DATE('2024-11-15 16:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 51.1, TO_DATE('2024-11-15 19:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 54.4, TO_DATE('2024-11-16 06:45:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 53.3, TO_DATE('2024-11-16 09:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 55.9, TO_DATE('2024-11-16 11:30:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 52.1, TO_DATE('2024-11-16 14:00:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 56.0, TO_DATE('2024-11-16 16:15:00', 'YYYY-MM-DD HH24:MI:SS')),
(1, 50.8, TO_DATE('2024-11-16 18:45:00', 'YYYY-MM-DD HH24:MI:SS'));
    """))
    session.commit()
    session.close()
    print("Sensor readings inserted successfully")


def insert_irrigation_history():
    session = Session()
    session.execute(text("""
        INSERT INTO "IrrigationHistory" (timestamp, status, humidity_value) 
        VALUES 
        (TO_DATE('2024-11-06 06:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 57.2),
        (TO_DATE('2024-11-06 09:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 50.4),
        (TO_DATE('2024-11-06 11:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 49.9),
        (TO_DATE('2024-11-06 14:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 52.6),
        (TO_DATE('2024-11-06 16:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 54.8),
        (TO_DATE('2024-11-06 19:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 47.1),
        (TO_DATE('2024-11-07 08:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 60.3),
        (TO_DATE('2024-11-07 10:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 55.0),
        (TO_DATE('2024-11-07 13:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 58.5),
        (TO_DATE('2024-11-07 15:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 45.7),
        (TO_DATE('2024-11-07 18:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 50.6),
        (TO_DATE('2024-11-08 07:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 53.8),
        (TO_DATE('2024-11-08 10:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 46.3),
        (TO_DATE('2024-11-08 12:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 59.1),
        (TO_DATE('2024-11-08 15:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 49.5),
        (TO_DATE('2024-11-08 18:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 55.2),
        (TO_DATE('2024-11-09 07:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 57.6),
        (TO_DATE('2024-11-09 09:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 52.1),
        (TO_DATE('2024-11-09 12:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 50.4),
        (TO_DATE('2024-11-09 14:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 48.7),
        (TO_DATE('2024-11-09 16:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 51.3),
        (TO_DATE('2024-11-09 19:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 46.2),
        (TO_DATE('2024-11-10 06:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 54.1),
        (TO_DATE('2024-11-10 08:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 49.8),
        (TO_DATE('2024-11-10 11:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 58.7),
        (TO_DATE('2024-11-10 13:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 45.4),
        (TO_DATE('2024-11-10 16:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 52.0),
        (TO_DATE('2024-11-10 18:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 50.9),
        (TO_DATE('2024-11-11 08:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 56.2),
        (TO_DATE('2024-11-11 10:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 48.5),
        (TO_DATE('2024-11-11 13:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 53.7),
        (TO_DATE('2024-11-11 15:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 47.3),
        (TO_DATE('2024-11-11 17:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 51.8),
        (TO_DATE('2024-11-12 06:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 54.5),
        (TO_DATE('2024-11-12 09:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 49.1),
        (TO_DATE('2024-11-12 11:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 57.3),
        (TO_DATE('2024-11-12 14:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 50.0),
        (TO_DATE('2024-11-12 16:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 53.5),
        (TO_DATE('2024-11-12 19:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 48.2),
        (TO_DATE('2024-11-13 07:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 60.1),
        (TO_DATE('2024-11-13 09:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 55.9),
        (TO_DATE('2024-11-13 11:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 58.4),
        (TO_DATE('2024-11-13 13:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 46.5),
        (TO_DATE('2024-11-13 16:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 50.8),
        (TO_DATE('2024-11-13 18:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 47.9),
        (TO_DATE('2024-11-14 08:30:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 54.6),
        (TO_DATE('2024-11-14 10:45:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 52.3),
        (TO_DATE('2024-11-14 13:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 51.7),
        (TO_DATE('2024-11-14 15:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Desligado', 50.2),
        (TO_DATE('2024-11-14 18:00:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 53.4),
        (TO_DATE('2024-11-15 07:15:00', 'YYYY-MM-DD HH24:MI:SS'), 'Ligado', 55.9);
    """))
    session.commit()
    session.close()
    print("Irrigation history inserted successfully")


def insert_nutrients_sensor_readings():
    data = [
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 10.5, 'irrigation': 1},
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 9.6, 'irrigation': 1},
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 9.3, 'irrigation': 1},
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 9.7, 'irrigation': 1},
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 9.2, 'irrigation': 1},
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 9.4, 'irrigation': 1},
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 9.0, 'irrigation': 1},
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 8.8, 'irrigation': 1},
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 8.8, 'irrigation': 1},
        {'temperature': -14.8, 'humidity': 2.5, 'ph': 8.5, 'irrigation': 1}

    ]
    irrigation = False
    random_value = lambda: round(random.uniform(-40.0, 50.9), 2)
    for x in range(1, 5000):
        humidity = random_value()
        if humidity < 30.0:
            irrigation = True
        else:
            irrigation = False

        new_data = {'temperature': random_value(), 'humidity': random_value(), 'ph': random_value(), 'irrigation': irrigation}
        data.append(new_data)

    for reading in data:
        insert_nutrient_history(
            reading['temperature'],
            reading['humidity'],
            reading['ph'],
            reading['irrigation']
        )


def insert_weather_historical_data():
    with open('../db/weatherHistory.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            date_register = row['Formatted Date']
            summary =  row['Summary']
            precip_type = row['Precip Type']
            temperature = row['Temperature (C)']
            apparent_temperature = row['Apparent Temperature (C)']
            humidity = row['Humidity']
            wind_speed = row['Wind Speed (km/h)']
            wind_bearing = row['Wind Bearing (degrees)']
            visibility_km = row['Visibility (km)']
            loud_cover = row['Loud Cover']
            pressure = row['Pressure (millibars)']
            daily_summary = row['Daily Summary']
            import_weather_historical_data(
                date_register,
                summary,
                precip_type,
                temperature,
                apparent_temperature,
                humidity,
                wind_speed,
                wind_bearing,
                visibility_km,
                loud_cover,
                pressure,
                daily_summary
            )


if __name__ == "__main__":
    # Create all tables
    Base.metadata.create_all(engine)
    print("All tables created successfully")

    # Insert sample data
    # insert_producers()
    # insert_crops()
    # insert_sensors()
    # insert_sensor_readings()
    # insert_irrigation_history()
    insert_nutrients_sensor_readings()
    # insert_weather_historical_data()
