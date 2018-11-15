from flask import Flask, render_template, redirect , session ,request , redirect , url_for,jsonify
import requests
from app.forms import LoginForm,CiudadForm
from Meteo import Meteo
from Pistas import Pistas

app = Flask(__name__)

m = Meteo()
p = Pistas()


@app.route('/')
def inicio():
    return jsonify(status="Ok")

@app.route('/web' ,methods=['GET', 'POST'])
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


@app.route('/tiempo',methods=['GET', 'POST'])
def dos():
    weather=None
    city=None
    descripcion = None
    
    city = 'Almeria,ES'
    weather = m.get_weather(city)
    descripcion = m.statusTiempo(weather)
    
    
    return jsonify(weather,descripcion)


@app.route('/pistas',methods=['GET','POST'])
def pistas():

    pistas = p.pistasOperativas()

    return jsonify(pistas)


    
