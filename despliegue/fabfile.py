# Import para importar la API de fabric
from fabric.api import *


# INICIAMOS SISTEMA WEB MEDIANTE GUNICORN
def Iniciar():
    
    # Iniciamos el servicio web mediante "gunicorn" en el puerto elegido 80
    run('cd Proyecto-IV/app/ && sudo gunicorn main:app -b 0.0.0.0:80')

# BORRAMOS ANTIGUO CODIGO
def Borrar():

    # Borramos antiguo codigo
    run('rm -rf Proyecto-IV')


# BORRA Y VUELVE A DESCARGAR EL NUEVO CODIGO 
def Actualizar():

    # Borramos antiguo codigo
    Borrar()

    # Descargamos nuevo repositorio
    run('git clone https://github.com/vaderrama/Proyecto-IV.git')

    # Instalamos los requirements necesarios para el microservicio
    run('pip3 install -r Proyecto-IV/requirements.txt')


