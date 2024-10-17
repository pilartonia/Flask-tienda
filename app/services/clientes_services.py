from app import db, bcrypt
from app.models.clientes_model import Clientes


class ClientService:
    @staticmethod
    def create_client(nombre_cliente, telefono):
        print(nombre_cliente)
        print(telefono)
        # Crear un nuevo objeto cliente
        client = Clientes(nombre_cliente=nombre_cliente, telefono=telefono)
        
        # Añadir el nuevo cliente a la base de datos
        db.session.add(client)
        db.session.commit()
        
        return client  # Retornar el cliente recién creado
    
    @staticmethod
    def get_all_clients():
        # Recuperar todos los registros de la tabla clientes
        return Clientes.query.all()

    @staticmethod
    def get_client_by_clientId(id_cliente):
        # Filtrar clientes por su id (id_cliente)
        return Clientes.query.filter_by(id_cliente=id_cliente).first()

    @staticmethod
    def update_client(id_cliente, new_data):
        # Buscar al cliente por su id
        client = ClientService.get_client_by_clientId(id_cliente)
        if not client:
            # Si no se encuentra el cliente, lanzar una excepción
            raise ValueError('client not found')

        # Si se proporciona un nuevo nombre de cliente
        if 'nombre_cliente' in new_data:
            # Obtener el nuevo nombre del cliente
            nuevo_nombre = new_data['nombre_cliente']
            client.nombre_cliente = nuevo_nombre
        
                # Si se proporciona un nuevo nombre de cliente
        if 'telefono' in new_data:
            # Obtener el nuevo nombre del cliente
            nuevo_telefono = new_data['telefono']
            client.telefono = nuevo_telefono

        # Guardar los cambios en la base de datos
        db.session.commit()

    @staticmethod
    def delete_client(id_cliente):
        # Buscar al cliente por id
        client = ClientService.get_client_by_clientId(id_cliente)
        if not client:
            # Si no se encuentra el cliente, lanzar una excepción
            raise ValueError('client not found')

        # Eliminar el cliente de la base de datos
        db.session.delete(client)
        db.session.commit()
