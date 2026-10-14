from dotenv import load_dotenv
import os
import requests
load_dotenv()

cheie_api_key = os.getenv("API_KEY")
url = "https://api.openweathermap.org/data/2.5/weather?"
raspuns = requests.get(url,params={
    'lat': 46.556881,
    'lon': 26.898324,
    'appid':cheie_api_key}).json()

print(raspuns)