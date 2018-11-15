from flask import render_template, request, redirect, url_for, jsonify
import requests
import json
import os


class Pistas:


    def __init__(self):
        
        if os.path.exists('app/pistas.json'):
            with open('app/pistas.json', 'r') as f:
                pistas = json.load(f)

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
                devolver = i
            return devolver

    def pistasOperativas(self):
    
        """Creamos array con las pistas operativas en este momento"""
        operativas=[]
        
        for i in self.pistas:
            if i["operativa"] == "True":
                operativas.append(i)

        return operativas



    def pistasDificultad(self, dificultad):
        """Creamos array con las pistas segun la dificultad y si estan operativas"""
        
        
        return pistas
    
    def pistasLongitud(self, longitud):

        """Creamos array de pistas con las pistas que superen la longitud introducida"""
        
        return pistas
