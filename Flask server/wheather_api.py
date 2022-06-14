import requests
import json
from datetime import datetime
DayInWeek = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]

icons_id = {
	804: "https://cdn-icons-png.flaticon.com/512/1163/1163726.png", # Clouds - overclouds
	806: "https://cdn-icons-png.flaticon.com/512/2675/2675879.png", # Clouds- broken clouds
	806: "https://cdn-icons-png.flaticon.com/512/6974/6974833.png" # Clear - clear sky
}


def api_req(coordinations):
	# coordinations = {"lat": 50.22622179742758, "lon": 14.870976579184042}
	# e.g. a5cf6fe06555bdad19e9aedb13d8e5a8
	lat = coordinations["lat"]
	lon = coordinations["lon"]
	api_key = 'Token'
	api_current = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'
	api_forecast = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=daily&units=metric&appid={api_key}'

	response = requests.get(api_current)
	# print(response.json())
	result = response.json()
	response_forecast = requests.get(api_forecast)
	forecast = response_forecast.json()
	return forecast