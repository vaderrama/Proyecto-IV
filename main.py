
#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import flask
from flask import render_template

import forms

app = Flask(__name__)

app.route('/' , '/index')
def Login():
    comment_form = forms.Formulario()
    title = "SnowMet. Tu app de Snow"
    return render_template ( 'index.html', title = title , form=comment_form )



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['usuario'] = request.form['usuario']
    return redirect(url_for('index'))


@app.route('/logout', methods=['GET','POST'])
def logoute():
    if request.method == 'POST':
        session.pop('usuario', None)
    return redirect(url_for('index'))



