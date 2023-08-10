import requests
from datetime import datetime
def lat_lon(place):
    data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=5&appid=7b02f9f1a037bf6848cc8f4240c4989c")
    data = data.json()[0]
    lat=data["lat"]
    lon=data["lon"]
    return lat, lon

def get_weather_data(place, days):
    lat, lon = lat_lon(place)
    data = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=7b02f9f1a037bf6848cc8f4240c4989c")
    data = data.json()
    date = []
    temp = []
    weather = []
    for i in data["list"][:(8*days)]:
        date.append(datetime.strptime(i["dt_txt"], "%Y-%m-%d %H:%M:%S"))
        temp.append(i["main"]["temp"])
        weather.append(i["weather"][0])
    return date, temp, weather