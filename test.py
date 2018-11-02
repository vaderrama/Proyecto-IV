import pytest
from app.forms import *
from app.meteoclass import *


def test_form(self):
    self.assertIsInstance(self.CiudadForm(Form),city, "Formulario city creado correctamente")

def test_inicializar():
    n=meteo("almeria,ES" , "20" , "nublado" , "30" , "30" , "10d")
    assert isinstance(n,meteo), "Error al inicializar"

def test_getweather():
    weather = get_weather("Almeria, ES")
    if type(weather) == type(dict):
        pass

def test_inicio():
    n = inicio();
    if assert n != "OK", "Error al iniciar"

def test_status():
    devol = None
    weather = get_weather("Pradollano, ES")
    devol = statusTiempo ( weather )
    assert devol == None, "Error al tener un Status "
