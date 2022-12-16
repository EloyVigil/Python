from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key= '123456'

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('/index.html')

@app.route('/results', methods=['POST'])
def results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('results.html')

@app.route('/display')
def display():
    return redirect('/results')

if __name__=="__main__":
    app.run(debug=True)

