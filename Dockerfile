FROM python:2.7-slim

MAINTAINER Juan <juanalvarez@correo.ugr.es>
WORKDIR app/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 80
CMD cd app && gunicorn main:app 