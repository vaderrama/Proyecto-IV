from flask import render_template, request, redirect, url_for, jsonify
import requests
import json


class Meteo:


    def __init__(self):
        self.city = None
        self.temperature = None
        self.description = None
        self.wind = None
        self.humidity = None
        self.icon = None

    def crear_ciudad(self , city , temperature , description  ,wind , humidity , icon):
        self.city = city
        self.temperature = temperature
        self.description = description
        self.wind = wind
        self.humidity = humidity
        self.icon = icon
    
    
    def get_weather(self,city):
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



    def statusTiempo(self,weather):
        status=None
        tmp = weather["temperature"]
        viento = weather["wind"]
        hume = weather["humidity"]
        
        
        if tmp <= 2 and viento > 40 and hume > 50:
            status = ' Las probabilidades de que las pistas esten cerradas o no se pueda practicar deporte sin riesgos son muy altas'

        if tmp >0 and tmp < 15 and viento > 0 and viento < 10  and hume > 20 and hume < 100:
            status = ' Las condiciones son idoneas. Disfruta del dia! '
    
    
        if tmp > 12 and tmp < 25 and viento < 5:
            status = 'Las condiciones son favorables , pero la nieve estara blanda'
        
        if tmp == None and viento == None and hume == None and wind == None:
            status = ' El servicio de estatus personalizado no esta funcionando. Espere unos minutos. '
        
            
        if tmp > -5 and tmp < 5 and viento > 30 :
            status = 'El viento en zonas altas puede ser fuerte. Las rachas pueden superar los 60km/h. Recomendado no subir a zonas altas.'
        
        if tmp < -5 and viento > 10 and viento < 30 and hume < 50 :
            status = ' Evite zonas expuestas , la temperatura podria ser muy baja y las pistas podrian estar congeladas '
        
        if tmp >0 and tmp < 10 and viento > 0 and viento < 60 and hume > 0 and hume < 100:
            status = ' Evite zonas altas y expuestas , las condiciones son favorables en zonas bajas pero en zonas altas el viento podria aumentar considerablemente ' 
        
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
