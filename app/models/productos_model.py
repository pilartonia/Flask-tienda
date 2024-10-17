from app import db

class Productos(db.Model):
    __tablename__="productos"

    id_producto = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Clave primaria de la tabla
    nombre_producto = db.Column(db.String(100), unique=True, nullable=False)  
    cantidad=db.Column(db.Integer,nullable=False)
    precio=db.Column(db.Float,nullable=False)

def __init__(self, nombre_producto, cantidad, precio):
    self.nombre_producto=nombre_producto
    self.cantidad=cantidad
    self.precio=precio