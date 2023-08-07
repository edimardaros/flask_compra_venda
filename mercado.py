from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db.init_app(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True) #auto incremento
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descrica = db.Column(db.String(length=2014), nullable=False, unique=True)

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
def page_produto():
    itens = [
        {'id': 1, 'nome': 'celular', 'cod_barra': '123515124124', 'preco': 1200},
        {'id': 2, 'nome': 'notebook', 'cod_barra': '5437574', 'preco': 5500},
        {'id': 3, 'nome': 'teclado', 'cod_barra': '99999999', 'preco': 99},
        {'id': 4, 'nome': 'monitor', 'cod_barra': '76586877', 'preco': 800}
    ]
    return render_template("produtos.html", itens=itens)