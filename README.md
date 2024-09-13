# Airflow Project

## Introduction

The aim of this project is to explore Airflow (workflow orchestration) by extracting weather data via OpenWeather API, do some data processing and load it to an AWS S3 bucket.

To extract data python *requests* HTTP library was used. This data, originaly as a JSON was transformed to a pandas dataframe. For more info on OpenWeather API check here: [OpenWeatherAPI]([https://dbdiagram.io/d/66a7bdb38b4bb5230ea778af](https://openweathermap.org/current))

To install and run Airflow, an AWS EC2 ubuntu instance was used.

