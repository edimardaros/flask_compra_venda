from mercado import db
from mercado import bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    senha = db.Column(db.String(), nullable=False)
    valor = db.Column(db.Integer, nullable=False, default=5000)
    itens = db.relationship('Item', backref='dono_user', lazy=True)

    @property
    def senhacrip(self):
        return self.senhacrip
    
    @senhacrip.setter
    def senhacrip(self, senha_texto):
        self.senha = bcrypt.generate_password_hash(senha_texto).decode('utf-8')

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True) #auto incremento
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descricao = db.Column(db.String(length=2014), nullable=False, unique=True)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Definir o que retornar quando chamar Item.query.all()
    def __repr__(self):
        return f"Item {self.nome}"