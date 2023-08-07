from flask import Flask, render_template


app = Flask(__name__)

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