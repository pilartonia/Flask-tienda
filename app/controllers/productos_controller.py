from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.productos_services import ProductService

# Crear un espacio de nombres (namespace) para los productos
product_ns = Namespace('products', description='Operaciones relacionadas con los productos')

# Definir el modelo de producto para la documentación de Swagger
product_model = product_ns.model('product', {
    'nombre_producto': fields.String(required=True, description='Nombre de producto'),
    'cantidad': fields.Integer(required=True, description='Cantidad de producto'),
    'precio': fields.Float(required=True, description='Precio del producto'),
})

# Definir el controlador de productos con decoradores para la documentación
@product_ns.route('/')
class ProductResource(Resource):
    @product_ns.doc('create_product') #etiqueta para documentación
    @product_ns.expect(product_model, validate=True)  # Decorador para esperar el modelo en la petición
    def post(self):
        data = request.get_json()  # Obtiene los datos en formato JSON del cuerpo de la solicitud
        product = ProductService.create_product(data['nombre_producto'], data['cantidad'], data['precio'])
        # Usamos jsonify para asegurarnos de que la respuesta siga el formato JSON válido.
        return jsonify({'message': 'Product created successfully', 'product': product.nombre_producto})

    @product_ns.doc('get_products')
    def get(self):
        products = ProductService.get_all_products()  # Llama al servicio para obtener todos los productos
        # Usamos jsonify para garantizar que la lista de productos se retorne como un JSON válido.
        return jsonify({'products': [product.nombre_producto for product in products]})  # Retorna solo los nombres de producto


@product_ns.route('/<int:id_producto>')
@product_ns.param('id_producto', 'El id del producto')
class ProductDetailResource(Resource):
    @product_ns.doc('delete_product')
    def delete(self, id_producto):
        ProductService.delete_product(id_producto)  # Llama al servicio para eliminar al producto
        # Usamos jsonify para enviar un mensaje de éxito en formato JSON.
        return jsonify({'message': 'product deleted successfully'})

    @product_ns.doc('update_product')
    @product_ns.expect(product_model, validate=True)
    def put(self, id_producto):
        new_data = request.get_json()  # Obtiene los nuevos datos para la actualización
        ProductService.update_product(id_producto, new_data)  # Llama al servicio para actualizar el producto
        # Usamos jsonify para enviar un mensaje de éxito en formato JSON.
        return jsonify({'message': 'product updated successfully'})

