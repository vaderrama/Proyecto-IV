from flask import render_template, request, redirect, url_for, jsonify
import requests
import json
import os


class Pistas:


    def __init__(self):
        
        with open('pistas.json', 'r') as f:
            self.pistas = json.load(f)

    
                    
    def pistaNueva(self , nombre , longitud  ,dificultad , operativa,description  ):
        self.nombre = nombre
        self.longitud = longitud
        self.dificultad = dificultad
        self.operativa = operativa
        self.description = description
    
    
    def getPistaNombre(self, nombre):
        pista = []
        
        for i in self.pistas:
            if i["nombre"] == nombre:
                pista.append(i)
                    
        return pista

    def pistasOperativas(self):
    
        """Creamos array con las pistas operativas en este momento"""
        operativas=[]
        
        for i in self.pistas:
            if i["operativa"] == "True":
                operativas.append(i)



        return operativas



    def pistasDificultad(self, dificultad):
        """Creamos array con las pistas segun la dificultad y si estan operativas"""
        pistas=[]
        
        for i in self.pistas:
            if i["operativa"] == "True":
                if i["dificultad"] == dificultad:
                    pistas.append(i)
        
        
        return pistas
    
    def pistasLongitud(self, longitud):
        """Creamos array de pistas con las pistas que superen la longitud introducida"""
        pistas=[]
        
        for i in self.pistas:
            intlong = int(i["longitud"])
            if intlong >= intlong2:
                pistas.append(i)
        
        
        return pistas



