from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado2.db"
db.init_app(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True) #auto incremento
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descricao = db.Column(db.String(length=2014), nullable=False, unique=True)

    # Definir o que retornar quando chamar Item.query.all()
    def __repr__(self):
        return f"Item {self.nome}"


@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
def page_produto():
    itens = Item.query.all()
    return render_template("produtos.html", itens=itens)