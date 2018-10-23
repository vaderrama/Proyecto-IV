import pytest
from app.main import get_weather


def test_get_weather():
    weather = get_weather("Almeria, ES")
    if type(weather) == type(dict):
        pass
