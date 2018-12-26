from flask import Flask, render_template, redirect , session ,request , redirect , url_for,jsonify
import requests
from Meteo import Meteo
from Pistas import Pistas


app = Flask(__name__)

m = Meteo()
p = Pistas()


@app.route('/',methods=['GET'])
def inicio():
    status={"status":"OK"}
    return jsonify(status)

@app.route('/status',methods=['GET'])
def inicio2():
    status={"status":"OK"}
    return jsonify(status)

"""
@app.route('/web' ,methods=['GET'])
def index():
    weather=None
    city=None
    descripcion = None
    
    form = CiudadForm(request.form)
    
    
    if request.method == 'POST':
        city=request.form['city']
        weather = m.get_weather(city)
        descripcion = m.statusTiempo(weather)
    
    
    return render_template('index.html', weather=weather,form=form , descripcion = descripcion )
"""

@app.route('/tiempo/<ciudad>',methods=['GET'])
def tiempo(ciudad):
    weather=None
    city=None
    descripcion = None
    
    city = ciudad
    weather = m.get_weather(city)
    descripcion = m.statusTiempo(weather)
    
    
    return jsonify(weather,descripcion)

@app.route('/tiempoEstaciones',methods=['GET'])
def tiempoEstaciones():

    text = 'Principales estaciones de Espana'
    
    city1 = 'Pradollano, ES'
    city2 = 'Andorra, ES'
    city3 = 'Cerler, ES'
    city4 = 'Baqueira, ES'
    
    weather1 = m.get_weather(city1)
    weather2 = m.get_weather(city2)
    weather3 = m.get_weather(city3)
    weather4 = m.get_weather(city4)

    descripcion1 = m.statusTiempo(weather1)
    descripcion2 = m.statusTiempo(weather2)
    descripcion3 = m.statusTiempo(weather3)
    descripcion4 = m.statusTiempo(weather4)


    return jsonify(text,weather1,descripcion1,weather2,descripcion2,weather3,descripcion3,weather4,descripcion4)



@app.route('/pistas',methods=['GET'])
def pistas():

    pistas = p.pistasOperativas()

    return jsonify(pistas)


@app.route('/pistas/<nombre>',methods=['GET'])
def pistaNombre(nombre):

    pistas = p.getPistaNombre(nombre)
    
    return jsonify(pistas)

@app.route('/pistas/dificultad/<color>',methods=['GET'])
def pistaColor(color):

    pistas = p.pistasDificultad(color)

    return jsonify(pistas)


@app.route('/pistas/<longitud>',methods=['GET'])
def pistaLongitud(longitud):
    intlong=int(longitud)
    pistas = p.pistasLongitud(intlong)

    return jsonify(pistas)


