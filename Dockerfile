# Version de python que se va a utilizar
FROM python:2.7-slim
# Informacion relativa al creador
MAINTAINER Juan <juanalvarez@correo.ugr.es>

# Definimos /app como directorio de trabajo
WORKDIR app/

# Copiamos el archivo requirements .txt al directorio raiz del contenedor
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el contenido del directorio actual al contenedor en /app
COPY . /app

# Abrimos el puerto 80
EXPOSE 80

# Ejecutamos con gunicorn nuestro main 
CMD cd app && gunicorn main:app 