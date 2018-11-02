import pytest
import requests
from app.forms import CiudadForm
from app.meteoclass import *
from app.main import get_weather , inicio , statusTiempo

"""
def test_form():
    form = None
    form = CiudadForm(request.form)
    assert form == None,"Formulario city creado correctamente"
    """
"""
def test_inicializar(self):
    self.city = 'Almeria, ES'
    self.temperature = 20
    self.wind = 20
    self.humidity = 20
    self.icon = '10d'
"""
def test_getweather():
    weather = get_weather('Almeria, ES')
    if type(weather) == type(dict):
        pass
"""
def test_inicio():
    n = inicio()
    assert n != None, "Error al iniciar"
"""
def test_status():
    devol = None
    weather = get_weather('Pradollano, ES')
    devol = statusTiempo(weather)
    assert devol == None, "Error al tener un Status "
