import pytest
import requests
from app.Meteo import Meteo
from app.Pistas import Pistas

m = Meteo()


def test_inicializar():
    n=Meteo()
    assert isinstance(n,Meteo), "Error al inicializar"

def test_getweather():
    weather = m.get_weather('Almeria, ES')
    if type(weather) == type(dict):
        pass


def test_status():
    devol = None
    weather = m.get_weather('Pradollano, ES')
    devol = m.statusTiempo(weather)
    assert devol != None, "Error al tener un Status "


def test_inicializarPistas():
    p = Pistas()
    assert isinstance(p,Pistas),"Error al inicializar"
    
"""
def test_pistasOperativas():
    operativas=[]
    p = Pistas()
    operativas = p.pistasOperativas()
    assert operativas != [], "Error al tener pistas operativas"
"""
