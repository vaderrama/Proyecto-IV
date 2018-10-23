from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class CiudadForm(Form):
    city = StringField('Ciudad ( Ej: Granada, ES )', [validators.Length(min=4, max=25)])




