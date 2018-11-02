from flask import Flask, render_template, redirect , session ,request , redirect , url_for,jsonify
import requests
from app.forms import LoginForm,CiudadForm
import meteoclass

app = Flask(__name__)


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
        'wind': r['wind']['speed'],
        'humidity' : r['main']['humidity'],
    }
    return weather

@app.route('/')
def inicio():
    return jsonify(status="Ok")

def statusTiempo(weather):
        status = None
        tmp = weather["temperature"]
        viento = weather["wind"]
        hume = weather["humidity"]
        
        
        if tmp <= 2 and viento > 40 and hume > 50:
            status = ' Las probabilidades de que las pistas esten cerradas o no se pueda practicar deporte sin riesgos son muy altas'

        if tmp >0 and tmp < 5 and viento > 0 and viento < 10  and hume > 20 and hume < 60:
            status = ' Las condiciones son idoneas. Disfruta del dia! '
        
        
        return status


@app.route('/app' ,methods=['GET', 'POST'])
def index():
    weather=None
    city=None
    descripcion = None
    
    form = CiudadForm(request.form)
    
    
    if request.method == 'POST':
        city=request.form['city']
        weather = get_weather(city)
        descripcion = weather["description"]
    
    

    
    

    
    return render_template('index.html', weather=weather,form=form , descripcion = descripcion )


