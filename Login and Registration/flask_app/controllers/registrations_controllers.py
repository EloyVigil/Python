from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.registration_models import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    # checking to see if user in session if not it will return false and redirect to home page
    if not "user_id" in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/reg_user', methods=['POST'])
def save_user():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password": pw_hash,
    }
    user_id = User.save_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/validate', methods=['POST'])
def validate():
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        "email":request.form['email'],
        "password":request.form['password']
    }
    return redirect('/dashboard')

@app.route('/login', methods=["POST"])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')