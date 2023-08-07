from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/sobre/<usuario>')
def sobre(usuario):
    return render_template("home.html")