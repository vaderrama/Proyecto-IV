from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
app = Flask(__name__)


class meteo:

    def __init__(city , temperature , description , wind , humidity, icon ):
        self.city = city
        self.temperature = temperature
        self.description = description
        self.wind = wind
        self.humidity = humidity
        self.icon = icon

    
    def getWeather(city):
        
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}' \
        '&units=metric&appid=56f9b5c11b1436358ed721716d4e942f'
    
        r = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'wind': r['wind']['speed'],
            'humidity' : r['main']['humidity'],
    
        }

        return weather



    def statusTiempo(weather):
        tmp = weather["temperature"]
        viento = weather["wind"]
        hume = weather["humidity"]
        
        
        if tmp <= 2 and viento > 40 and hume > 50:
            status = ' Las probabilidades de que las pistas esten cerradas o no se pueda practicar deporte sin riesgos son muy altas'

        if tmp >0 and tmp < 5 and viento > 0 and viento < 10  and hume > 20 and hume < 60:
            status = ' Las condiciones son idoneas. Disfruta del dia! '
    

        return status
            
            
    
    def getCity(self):
        return self.city

    def getHumidity(self):
        return self.humidity

    def getTemperatura(self):
        return self.temperature

    def getWind(self):
        return self.wind

    def getDescripcion(self):
        return self.description
