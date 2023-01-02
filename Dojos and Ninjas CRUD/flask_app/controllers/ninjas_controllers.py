from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja_models import Ninja
from flask_app.models.dojo_models import Dojo


@app.route('/ninja')
def ninja():
    return render_template('ninjas.html',  dojos = Dojo.get_dojos())

@app.route('/new_ninja', methods = ['POST'])
def new_ninja():
    print("hi")
    data = {
        "dojo_id" : request.form['dojo'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age']
    }
    Ninja.add_ninja(data)
    return redirect('/ninja')