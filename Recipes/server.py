from flask_app.controllers import recipes_controllers, users_controllers
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)