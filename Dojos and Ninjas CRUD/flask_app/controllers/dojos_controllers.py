from flask import render_template, redirect, request

from flask_app import app

from flask_app.models.dojo_models import Dojo
from flask_app.models.ninja_models import Ninja

@app.route('/new/dojo')
def dojo():
    return render_template('dojo.html', dojos = Dojo.get_dojos())

@app.route('/dojo/and/ninjas/<int:id>')
def dojo_ninja(id):
    data= {
        "id": id
    }
    dojo = Dojo.get_all(data)
    return render_template('dojoandninjas.html', dojo = dojo)    


@app.route('/new_dojo', methods=['POST'])
def new_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/new/dojo')