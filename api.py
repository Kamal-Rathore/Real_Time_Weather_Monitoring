import requests

API_KEY = 'f3b0dc48291064c470b17ba56eff500b'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city):
    
    response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
    return response.json() if response.status_code == 200 else None

