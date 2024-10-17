from app import db, bcrypt
from app.models.productos_model import Productos


class ProductService:
    @staticmethod
    def create_product(nombre_producto, cantidad, precio):
        # Crear un nuevo objeto producto
        product = Productos(nombre_producto=nombre_producto, cantidad=cantidad, precio=precio)
        
        # Añadir el nuevo producto a la base de datos
        db.session.add(product)
        db.session.commit()
        
        return product  # Retornar el producto recién creado
    
    @staticmethod
    def get_all_products():
        # Recuperar todos los registros de la tabla Productos
        return Productos.query.all()

    @staticmethod
    def get_product_by_productId(id_producto):
        # Filtrar productos por su id (id_producto)
        return Productos.query.filter_by(id_producto=id_producto).first()


    @staticmethod
    def update_product(id_producto, new_data):
        # Buscar al producto por su id
        product = ProductService.get_product_by_productId(id_producto)
        if not product:
            # Si no se encuentra el producto, lanzar una excepción
            raise ValueError('product not found')

        # Si se proporciona un nuevo nombre de producto
        if 'nombre_producto' in new_data:
            # Obtener el nuevo nombre del producto
            nuevo_nombre_producto = new_data['nombre_producto']
            product.nombre_producto = nuevo_nombre_producto
        
        # Si se proporciona una nueva cantidad de producto
        if 'cantidad' in new_data:
            # Obtener la nueva cantidad del producto
            nueva_cantidad = new_data['cantidad']
            product.cantidad = nueva_cantidad

        # Si se proporciona un nuevo precio de producto
        if 'precio' in new_data:
            # Obtener el nuevo precio del producto
            nuevo_precio = new_data['precio']
            product.precio = nuevo_precio

        # Guardar los cambios en la base de datos
        db.session.commit()

    @staticmethod
    def delete_product(id_producto):
        # Buscar al producto por id
        product = ProductService.get_product_by_productId(id_producto)
        if not product:
            # Si no se encuentra el producto, lanzar una excepción
            raise ValueError('product not found')

        # Eliminar el producto de la base de datos
        db.session.delete(product)
        db.session.commit()
