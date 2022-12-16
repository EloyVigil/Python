from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def hello_world():
    return render_template("index.html")

@app.route('/play/<int:num>')
def play(num):
    return render_template("index1.html", box = num)

@app.route('/play/<int:num>/<color>')
def playmore(num, color):
    return render_template("index2.html", box = num, color = color)


if __name__=="__main__":
    app.run(debug=True)

