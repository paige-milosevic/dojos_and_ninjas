from unicodedata import name
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/ninjas')
def newNinja():
    return render_template('ninjas.html',dojos=Dojo.getAll(),ninjas=Ninja.getAll())

@app.route('/ninja/new', methods=['POST'])
def createNinja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect('/')

