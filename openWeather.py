#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import sys

current = 'http://api.openweathermap.org/data/2.5/weather'
forecast = 'http://api.openweathermap.org/data/2.5/forecast'

params = {
    'q': 'Auckland',
    'units': 'metric',
    'lang': 'en',
    'appid': 'f189a5cf95c445791f2c022d515c1874'
}

try:
    data_current = requests.get(current, params=params).json()
    data_forecast = requests.get(forecast, params=params).json()
except:
    print('Ошибка подключения к интернету')
    sys.exit(1)

template_header = "Температура в {}e \n" \
                  "\n\tтекущая температура: {}\u00b0 \n\t{}, влажность: {}%"

for cur_data in data_current['weather']:
    print('\n', template_header.format(
        data_current['name'],
        data_current['main']['temp'],
        cur_data['description'],
        data_current['main']['humidity']))

wind_direction = data_current['wind']['deg']
if wind_direction == 90:
    wind_direction = 'Восточный'
elif wind_direction == 180:
    wind_direction = 'Южный'
elif wind_direction == 270:
    wind_direction = 'Западный'
elif 0 < wind_direction < 90:
    wind_direction = 'Северо-восточный'
elif 90 < wind_direction < 180:
    wind_direction = 'Юго-восточный'
elif 180 < wind_direction < 270:
    wind_direction = 'Юго-западный'
elif 270 < wind_direction < 360:
    wind_direction = 'Северо-западный'
else:
    wind_direction = 'Северный'

template_wind = '\tСкорость ветра: {} м/с, {}\n'
print(template_wind.format(
    data_current['wind']['speed'],
    wind_direction))

template_forecast = 'Date: {}  Min: {}\u00b0 Max: {}\u00b0 {}\n'
for day_data in data_forecast['list'][2::8]:
    for weath in day_data['weather']:
        print(template_forecast.format(
            day_data['dt_txt'][0:10],
            format(day_data['main']['temp_min'], '.1f'),
            format(day_data['main']['temp_max'], '.1f'),
            weath['description']
        ))

print(' Данные на 12 часов дня')

# https://openweathermap.org/api
