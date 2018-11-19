FROM python:2.7-slim

MAINTAINER Juan <juanalvarez@correo.ugr.es>
WORKDIR app/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
CMD cd app && gunicorn main:app --log-file=- --bind 0.0.0.0:80