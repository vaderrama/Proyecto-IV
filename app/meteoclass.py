from flask import Flask
app = Flask(__name__)


class meteo: #fecha(dd ,mm, ññññ) / zonaDia ( mañana , tarde , noche )  / tiempo ( atmosferico , nieve , viento )

    def __init__(self , fecha , zonaDia , tiempo ):
        self.fecha = fecha
        self.zonaDia = zonaDia
        self.tiempo = tiempo


    def getFecha(self):
        return self.fecha

    def getZonaDia(self):
        return self.zonaDia

    def getTiempo(self):
        return self.tiempo


    def setFecha(fecha):
        self.fecha = fecha

    def set.zonaDia(zonaDia):
        self.zonaDia = zonaDia

    def setTiempo(tiempo):
        self.tiempo = tiempo
