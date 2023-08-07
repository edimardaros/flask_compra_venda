from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/sobre/<usuario>')
def sobre(usuario):
    return f"<h3>Sobre mim: {usuario}</h3>"