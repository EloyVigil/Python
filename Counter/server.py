from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key= '123456'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/counter')
def counter():
    if not 'counter' in session:
        session ['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

@app.route('/plus')
def countplus():
    session['counter'] += 1
    return redirect('/counter')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/counter')

if __name__=="__main__":
    app.run(debug=True)

