from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/flask')
def hi_flask():
    return "Hi Flask!"

@app.route('/say/michael')
def hi_michael():
    return "Hi Michael!"

@app.route('/say/john')
def hi_john():
    return "Hi John!"

@app.route('/repeat/35/hello')
def many_hello():
    return "Hello" * 35

@app.route('/repeat/80/bye')
def many_bye():
    return "Bye" * 80

@app.route('/repeat/99/dogs')
def many_dog():
    return "Dog" * 99



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

