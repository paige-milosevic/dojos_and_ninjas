from crypt import methods
from unicodedata import name
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojos import Dojo

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def allDojos():
    return render_template('dojos.html',dojos=Dojo.getAll())

@app.route('/dojo/create', methods=['POST'])
def createDojo():
    Dojo.save(request.form)
    return redirect('/')


@app.route('/dojo/<int:id>')
def getDojosNinjas(id):
    data = {
        "id": id
    }
    return render_template('dojosninjas.html', dojo=Dojo.getAllNinjas(data))
