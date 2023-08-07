from mercado import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True) #auto incremento
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descricao = db.Column(db.String(length=2014), nullable=False, unique=True)

    # Definir o que retornar quando chamar Item.query.all()
    def __repr__(self):
        return f"Item {self.nome}"