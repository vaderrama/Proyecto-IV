# Repositorio para el proyecto de la asignatura IV   


[![Build Status](https://travis-ci.org/vaderrama/Proyecto-IV.svg?branch=master)](https://travis-ci.org/vaderrama/Proyecto-IV)

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://snowmet.herokuapp.com/app)


## "SnowMet" Microservicio web 

Es proyecto consistira en el desarrollo de un microservicio web orientado al mundo del Snowboard. Donde trataremos en un principio el servicio de meteorologia de las distintas ciudades , asi como el de Sierra Nevada , indicando las caracteristicas concretas de este sitio. Utilizaremos para ello una API de [OpenWeatherMap](https://openweathermap.org/).

Nombre del proyecto: SnowMet

Desarrollado por : Juan Alvarez Carrasco

## Colaboración
Este proyecto sera unificado con el proyecto de [Alvarosanpal](https://github.com/Alvarosanpal/Proyecto_IV) , el cual se encargará de la gestion de equipamiento necesario , asi como su recomendacion personalizada.

Este servicio puede ser ampliado para mostrar capacidad de alquiler en nuestro servicio , asi como compra de forfeits o alquiler de profesores. 

    
## Herramientas utilizadas 

- Lenguaje de programacion : Python. Además HTML y CSS

- Como BD utilizaremos : MongoDB ( Posible cambio en un futuro )

- Framework : Flask

- Test : Pytest

- Integración Continua : Travis-CI

- Despliege : Heroku


## El porqué de este proyecto.

 El interes por aprender un nuevo lenguaje como Python, el cual me parece de un gran potencial ,  aplicandolo a un campo donde me siento bastante comodo como son los deportes. Ademas de poder crear un servicio de gran utilidad para el publico de este deporte en concreto. 



## Instalacion Necesaria 

Utilizaremos el siguiente comando para instalar las dependencias y modulos necesarios : $ pip install -r requirements.txt 

## Ejecucion de los test

Para ejecutar los test necesitamos usar el siguiente comando : $ pytest test.py

## Despliegue con Heroku

Hemos utilizado el sistema Heroku por su versatilidad a la hora de desplegar aplicaciones web de pequeña capacidad , así como su perfecta integración con GitHub y Travis-CI , lo que lo hace un servicio PaaS muy recomendando.

Para proceder a su despliegue , hemos vinculado nuestro repositorio de GitHub con el sistema Heroku desde su pagina web , donde de manera muy intuitiva podemos enlazarlo y al hacer click en la pestaña **Deploy Branch** , el servicio cargará nuestro repositorio en su sistema para poder desplegarla.

Despliegue : https://snowmet.herokuapp.com/ 

Despliegue ***< /app ( Microservicio **SnowMet** actualmente funcionando )> :*** https://snowmet.herokuapp.com/app
- ### Procfile

    En nuestro procfile disponemos de dos lineas :
        - En la primera linea se indica al procfile donde se encuentra nuestro archivo principal y como ejecutarlo , utilizamos el proceso **"web"**. Además del log
        - La segunda linea no la esta activada actualmente , ya que no la necesitamos por ahora.  ( "worker" )
        

## Descripción Clase y archivos principales

Actualmente esta app dispone de una clase llamada **meteoclass.py**  , la cual se encarga de la gestion de las variables referentes al clima , asi como su llamada a la API y la gestion de esta información. Esta clase tambien informa del estatus propio externo a la API.

Disponemos de una clase **forms.py** para la gestion de los formularios en nuestro sistema web. 

El fichero principal **main.py** se encarga de atender las peticiones de la app de manera directa. 

El sistema web esta alojado en las carpetas **templates** y **static**. Donde podremos encontrar las diferentes herramientas utilizadas para su correcta estructura , visualización y estilo.


## Avance SnowMet

Actualmente , el microservicio dispone de dos rutas :

****/app**** : En esta ruta , la aplicación despone de 4 menus en forma de botón. En ellos podemos acceder al "Home" , "Meteo" , "Equipacion" , "About".
            
            - Home : Directorio principal de la app. Breve descripción del proyecto
            - Meteo : Zona de analisis meteorológico , donde introduciendo una Ciudad podemos observar las distintas características de la climatologia. 
            - Equipación : Zona de ayuda , analisis y estimacion del mejor equipamiento necesario para tu nivel de habilidad. ( Parte correspondiente a nuestra Colaboracion [Equipamiento](https://github.com/Alvarosanpal/Proyecto_IV))
            - About : Información respecto al creador.

****/ , /status**** : En esta ruta se nos devuelve un JSON "OK" para poder visualizar el funcionamiento del sistema. 


