from app import db

class Clientes(db.Model):
    __tablename__="clientes"

    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Clave primaria de la tabla
    nombre_cliente = db.Column(db.String(100), unique=True, nullable=False)  
    telefono=db.Column(db.Integer,nullable=False)

def __init__(self, nombre_cliente, telefono):
    self.nombre_cliente=nombre_cliente
    self.telefono=telefono
    