from wtforms import Form
from wtforms import StringField , TextField
from wtf.fields.html5 import EmailField


class Formulario(Form):
    usuario = StringField ('username')
    passwd = StringField ( 'Contraseña' )






