from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError
from models import Producers, Crops, Sensors, SensorReadings, ApplicationAdjustments, IrrigationHistory, \
    NutrientHistory, WeatherHistoricalData
from database import Session
import requests
import os

def insert_producer(name, location, registration_date):
    session = Session()
    try:
        new_producer = Producers(name=name, location=location, registration_date=registration_date)
        session.add(new_producer)
        session.commit()
        print("Producer inserted successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting producer: {e}")
    finally:
        session.close()

def insert_crop(name, crop_type, id_producer):
    session = Session()
    try:
        new_crop = Crops(name=name, type=crop_type, id_producer=id_producer)
        session.add(new_crop)
        session.commit()
        print("Crop inserted successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting crop: {e}")
    finally:
        session.close()

def insert_sensor(sensor_type, id_crop):
    session = Session()
    try:
        new_sensor = Sensors(sensor_type=sensor_type, id_crop=id_crop)
        session.add(new_sensor)
        session.commit()
        print("Sensor inserted successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting sensor: {e}")
    finally:
        session.close()

def insert_sensor_reading(id_sensor, reading_value):
    session = Session()
    try:
        new_reading = SensorReadings(id_sensor=id_sensor, reading_value=reading_value)
        session.add(new_reading)
        session.commit()
        print("Sensor reading inserted successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting sensor reading: {e}")
    finally:
        session.close()

def insert_application_adjustment(water_quantity, nutrient_quantity, id_crop):
    session = Session()
    try:
        new_adjustment = ApplicationAdjustments(
            water_quantity=water_quantity,
            nutrient_quantity=nutrient_quantity,
            id_crop=id_crop
        )
        session.add(new_adjustment)
        session.commit()
        print("Application adjustment inserted successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting application adjustment: {e}")
    finally:
        session.close()

def insert_irrigation_history(timestamp, status, humidity_value):
    session = Session()
    try:
        new_history = IrrigationHistory(
            timestamp=timestamp,
            status=status,
            humidity_value=humidity_value
        )
        session.add(new_history)
        session.commit()
        print("Irrigation history record inserted successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting irrigation history record: {e}")
    finally:
        session.close()


def fetch_weather_forecast(city="São Paulo", country="BR"):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}&units=metric&lang=pt_br"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            print("Response content:", response.text)
            return []

        data = response.json()
        forecast_list = []

        
        for forecast in data.get('list', [])[:5]:  
            
            datetime_obj = datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S")
            formatted_datetime = datetime_obj.strftime("%d/%m/%Y %H:%M")

            forecast_list.append({
                "datetime": formatted_datetime,  
                "temp": forecast['main'].get('temp'),
                "humidity": forecast['main'].get('humidity'),
                "weather": forecast['weather'][0].get('description'),
                "rain": forecast.get('rain', {}).get('3h', 0)  
            })

        return forecast_list
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def insert_nutrient_history(temperature, humidity, ph, irrigation):
    session = Session()
    try:
        new_history = NutrientHistory(
            temperature=temperature,
            humidity=humidity,
            ph=ph,
            irrigation=irrigation
        )
        session.add(new_history)
        session.commit()
        print("Nutrient history record inserted successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting nutrient history record: {e}")
    finally:
        session.close()

def import_weather_historical_data(date_register,
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
                daily_summary):
    session = Session()
    try:
        new_data = WeatherHistoricalData(
            date_register=date_register,
            summary=summary,
            precip_type=precip_type,
            temperature=temperature,
            apparent_temperature=apparent_temperature,
            humidity=humidity,
            wind_speed=wind_speed,
            wind_bearing=wind_bearing,
            visibility_km=visibility_km,
            loud_cover=loud_cover,
            pressure=pressure,
            daily_summary=daily_summary
        )
        session.add(new_data)
        session.commit()
        print("Weather historical data inserted successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting weather historical data: {e}")
    finally:
        session.close()