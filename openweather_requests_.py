import pandas as pd
import requests


def openweather_etl():

    API_key = "xxx"
    lat = "44.34"
    lon = "10.99"
    units = "metric"
    openweather_api_request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units={units}"

    raw_weather_data = requests.get(openweather_api_request).json()

    # to extract data from the json we can use the .get function and add an empy dictionary, just in case the field no longer exists

    # extracted_data = {
    #    'dt': data.get('dt'),
    #    'timezone': data.get('timezone'),
    #    'lon': data.get('coord', {}).get('lon'),
    #    'lat': data.get('coord', {}).get('lat'),
    #    'temp': data.get('main', {}).get('temp'),
    #    'humidity': data.get('main', {}).get('humidity')

    # Or we can simply do it like this:

    extracted_data = {
        "dt": raw_weather_data["dt"],
        "timezone": raw_weather_data["timezone"],
        "lon": raw_weather_data["coord"]["lon"],
        "lat": raw_weather_data["coord"]["lat"],
        "temp": raw_weather_data["main"]["temp"],
        "humidity": raw_weather_data["main"]["humidity"],
    }

    df_data = pd.DataFrame([extracted_data])

    df_data.to_csv("s3://raul-airflow-etl-bucket/weather.csv")

    # print(df_data)
