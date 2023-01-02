from flask import render_template, redirect, request

from flask_app import app

from flask_app.models.user import User


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("indexform.html", users=users)

@app.route('/create_user', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/user')

@app.route('/user')
def show_user():
    
    return render_template("results.html", users = User.get_all())

@app.route('/user/info/<int:id>')
def user_info(id):
    data = {
        'id': id
    }
    users = User.select(data)
    return render_template("user_info.html", users=users)

@app.route('/user/edit/<int:id>')
def user_edit(id):
    data = {
        'id' : id
    }
    return render_template("edit_user.html", user = User.select(data))

@app.route('/delete_user/<int:id>')
def delete_user(id):
    delete_data = {
        'id': id
    }
    User.delete(delete_data)
    return redirect("/user")

@app.route('/update', methods=['POST'])
def update():
    
    User.edit(request.form)
    return redirect('/user')
