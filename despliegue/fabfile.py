
# Fabfile to:
#    - Borrar el microservicio
#    - Actualizar el microservicio
#    - Iniciar el microservicio

# Import Fabric's API module
from fabric.api import *

def Borrar():

    # Borramos antiguo codigo
    run('rm -rf Proyecto-IV')


def Actualizar():

    # Borramos antiguo codigo
    Borrar

    # Descargamos nuevo repositorio
    run('git clone https://github.com/vaderrama/Proyecto-IV.git')

    # Instalamos requirements
    run('pip3 install -r Proyecto-IV/requirements.txt')


def Iniciar():

     # Iniciamos el servicio web
     run('cd Proyecto-IV/app/ && sudo gunicorn main:app -b 0.0.0.0:80')

