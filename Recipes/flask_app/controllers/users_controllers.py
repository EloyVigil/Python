from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.user_model import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/save_user', methods=['POST'])
def save_user():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        **request.form,
        "password": pw_hash
    }
    user_id = User.save_user(data)
    session['user_id'] = user_id
    User.save_user
    return redirect('/all_recipes')

@app.route('/login', methods=["POST"])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/all_recipes')


@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')