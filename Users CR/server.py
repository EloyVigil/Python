from flask import Flask, render_template, redirect, request
# import the class from friend.py
from users import User
app = Flask(__name__)
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

if __name__ == "__main__":
    app.run(debug=True)