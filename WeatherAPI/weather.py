from datetime import datetime
from pydoc import describe
import requests

user_api_key = "d4091aca558594939f77ca596fd98e49"
location = input("Location: ")

api_url = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    location+"&appid="+user_api_key

api_request = requests.get(api_url)
api_data = api_request.json()


if(api_data['cod'] == '404'):
    print("No weather data found. Please check location")
else:
    temperature = api_data['main']['temp'] - 273.15
    feelsLikeTemperature = api_data['main']['feels_like'] - 273.15
    temp_min = api_data['main']['temp_min'] - 273.15
    temp_max = api_data['main']['temp_max'] - 273.15
    weather = api_data['weather'][0]['description']
    visibility = api_data['visibility']/1000.0
    windSpeed = api_data['wind']['speed'] * 3.6
    windDeg = api_data['wind']['deg']
    date_time = datetime.now().strftime("%d %b %Y || %H:%M:%S %p")

    print("--------------------------------------------")
    print(" Weather for {} || {}".format(location.upper(), date_time))
    print("--------------------------------------------\n")
    print("Temperature : {:.1f} °C".format(temperature))
    print("Feels Like : {:.1f} °C".format(feelsLikeTemperature))
    print("Minimum Temperature : {:.1f} °C\t\tMaximum Temperature : {:.1f} °C".format(
        temp_min, temp_max))
    print("Weather : "+weather)
    print("Visibility : {} kms".format(visibility))
    print("WindSpeed : {:.2f} km/sec at {} degrees".format(windSpeed, windDeg))
    print("----------------------------------------------")
