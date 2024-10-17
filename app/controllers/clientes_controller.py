from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.clientes_services import ClientService

# Crear un espacio de nombres (namespace) para los clientes
client_ns = Namespace('clients', description='Operaciones relacionadas con los clientos')

# Definir el modelo de cliento para la documentación de Swagger
client_model = client_ns.model('client', {
    'nombre_cliente': fields.String(required=True, description='Nombre de cliente'),
    'telefono': fields.Integer(required=True, description='Contacto de cliente'),
})

# Definir el controlador de clientes con decoradores para la documentación
@client_ns.route('/')
class clientResource(Resource):
    @client_ns.doc('create_client') #etiqueta para documentación
    @client_ns.expect(client_model, validate=True)  # Decorador para esperar el modelo en la petición
    def post(self):
        data = request.get_json()  # Obtiene los datos en formato JSON del cuerpo de la solicitud
        client = ClientService.create_client(data['nombre_cliente'], data['telefono'])
        # Usamos jsonify para asegurarnos de que la respuesta siga el formato JSON válido.
        return jsonify({'message': 'client created successfully', 'client': client.nombre_cliente})

    @client_ns.doc('get_clients')
    def get(self):
        clients = ClientService.get_all_clients()  # Llama al servicio para obtener todos los clientos
        # Usamos jsonify para garantizar que la lista de clientos se retorne como un JSON válido.
        return jsonify({'clients': [client.nombre_cliente for client in clients]})  # Retorna solo los nombres de cliento


@client_ns.route('/<int:id_cliente>')
@client_ns.param('id_cliente', 'El id del cliente')
class clientDetailResource(Resource):
    @client_ns.doc('delete_client')
    def delete(self, id_cliente):
        ClientService.delete_client(id_cliente)  # Llama al servicio para eliminar al cliento
        # Usamos jsonify para enviar un mensaje de éxito en formato JSON.
        return jsonify({'message': 'client deleted successfully'})

    @client_ns.doc('update_client')
    @client_ns.expect(client_model, validate=True)
    def put(self, id_cliente):
        new_data = request.get_json()  # Obtiene los nuevos datos para la actualización
        ClientService.update_client(id_cliente, new_data)  # Llama al servicio para actualizar el cliento
        # Usamos jsonify para enviar un mensaje de éxito en formato JSON.
        return jsonify({'message': 'client updated successfully'})