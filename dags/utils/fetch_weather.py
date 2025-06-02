from airflow.models import Variable
import os
import requests
import pandas as pd
from datetime import datetime, timezone

API_KEY = Variable.get("OPEN_WEATHER_API_KEY")
BASE_URL = Variable.get("OPEN_WEATHER_BASE_URL")

cities = [
    "Paris", "Berlin", "Madrid", "Rome", "Vienna", "Athens", "Warsaw", "Amsterdam", "Brussels", "Copenhagen",
    "Helsinki", "Oslo", "Stockholm", "Lisbon", "Prague", "Budapest", "Dublin", "Zagreb", "Ljubljana", "Bratislava",
    "Vilnius", "Riga", "Tallinn", "Bern", "Reykjavik", "Luxembourg", "Valletta", "Monaco", "Andorra la Vella",
    "San Marino", "Vaduz", "Skopje", "Sarajevo", "Belgrade", "Podgorica", "Tirana", "Chisinau", "Bucharest",
    "Sofia", "Kyiv"
]

def fetch_weather_data():

    weather_data = []

    for city in cities:
        
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        
        try:

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            record = {
            "id": data["weather"][0]["id"],
            "city_name": data.get("name"),
            "main": data["weather"][0]["main"],
            "date_time": datetime.now(timezone.utc),
            "description": data["weather"][0]["description"],
            "main_temp": data["main"]["temp"],
            "main_feels_like": data["main"]["feels_like"],
            "main_temp_min": data["main"]["temp_min"],
            "main_temp_max": data["main"]["temp_max"],
            "main_pressure": data["main"]["pressure"],
            "main_humidity": data["main"]["humidity"],
            "main_sea_level": data["main"].get("sea_level"),
            "main_grnd_level": data["main"].get("grnd_level"),
            "wind_speed": data["wind"]["speed"],
            "wind_deg": data["wind"].get("deg"),
            "wind_gust": data["wind"].get("gust"),
            "clouds_all": data["clouds"]["all"],
            "icon": data["weather"][0]["icon"],
            "base": data.get("base"),
            "visibility": data.get("visibility"),
            "dt": data.get("dt"),
            "timezone": data.get("timezone"),
            "cod": data.get("cod"),
            "coord_lon": data["coord"]["lon"],
            "coord_lat": data["coord"]["lat"],
            "sys_country": data["sys"]["country"],
            "sys_sunrise": data["sys"]["sunrise"],
            "sys_sunset": data["sys"]["sunset"],
            "sys_type": data["sys"].get("type"),
            "sys_id": data["sys"].get("id")
             }

            weather_data.append(record)

        except Exception as e:
            print(f"Failed for {city}: {e}")

    weather_data_dataframe = pd.DataFrame(weather_data)

    file_path = f"data/{datetime.now(timezone.utc).strftime('%Y-%m-%d_%H-%M-%S')}_weather_data.csv"

    weather_data_dataframe.to_csv(file_path, index=False)

    return file_path