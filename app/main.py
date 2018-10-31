from flask import render_template, flash, redirect , session ,request , redirect , url_for,jsonify
import requests
from forms import LoginForm,CiudadForm
from app import app





@app.route('/logout', methods=['GET','POST'])
def logoute():
    if request.method == 'POST':
        session.pop('username', None)
    return redirect(url_for('index'))



def get_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}' \
        '&units=metric&appid=56f9b5c11b1436358ed721716d4e942f'
    
    r = requests.get(url.format(city)).json()
    weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    return weather

@app.route('/')
def inicio():
    return jsonify(status="Ok")


@app.route('/app' ,methods=['GET', 'POST'])
def index():
    weather=None
    form = CiudadForm(request.form)
    
    
    if request.method == 'POST':
        city=request.form['city']
        weather = get_weather(city)
        print(weather)
    
    
    
    return render_template('index.html', weather=weather,form=form)


