from dotenv import load_dotenv
import os
import requests
load_dotenv()

cheie_api_key = os.getenv("API_KEY")
url = "https://api.openweathermap.org/data/2.5/weather?"
raspuns = requests.get(url, params={
    'lat': 46.556881,
    'lon': 26.898324,
    'appid': cheie_api_key,
    'units': 'metric',
    'lang': 'ro'
}).json()

url_geocoding = "http://api.openweathermap.org/geo/1.0/direct?"
raspuns_geoconding = requests.get(url_geocoding, params={
    'q': "Bacau",
    'appid': cheie_api_key
}).json()


    
starea_vremii = raspuns['weather'][0]['main']
temperatura = raspuns['main']['temp']
viteza_vant = raspuns['wind']['speed']