from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_migrate import Migrate
from .config import Config

# Inicializamos las extensiones globalmente para luego asociarlas a la app en la función create_app
db = SQLAlchemy()  # Para la interacción con la base de datos usando SQLAlchemy
migrate = Migrate()  # Para gestionar las migraciones de la base de datos
bcrypt = Bcrypt()  # Para el hash y verificación de contraseñas de los usuarios
jwt = JWTManager()  # Para la gestión de tokens JWT en la autenticación

def create_app():
    """Función factory para crear la aplicación Flask y configurar sus componentes."""
    
    # Creamos una instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Cargamos la configuración de la aplicación desde el archivo de configuración
    app.config.from_object(Config)

    # Inicializamos las extensiones con la aplicación
    db.init_app(app)  # Inicializar SQLAlchemy con la app
    bcrypt.init_app(app)  # Inicializar Bcrypt con la app
    jwt.init_app(app)  # Inicializar JWTManager con la app
    migrate.init_app(app, db)  # Inicializar Migrate con la app y la base de datos

    # Autorizador JWT para integrar con la documentación Swagger
    authorizations = {
        'Bearer': {
            'type': 'apiKey',  # Tipo apiKey define que el token JWT se envía en el encabezado de la solicitud
            'in': 'header',  # El token JWT se debe enviar en el encabezado de la solicitud HTTP
            'name': 'Authorization',  # Nombre del campo del encabezado HTTP para el token
            'description': 'JWT Bearer token. Ejemplo: "Bearer {token}"'  # Instrucción sobre cómo enviar el token
        }
    }

    # Configuramos la API Flask-RESTX, que nos ayuda a crear endpoints RESTful con documentación Swagger integrada
    api = Api(
        app,  # La aplicación Flask en la que registramos la API
        title='API de clientes y productos',  # Título para la documentación Swagger
        version='1.0',  # Versión de la API
        description='API para gestión de clientes y productos',  # Descripción de la API
        authorizations=authorizations,  # Añadimos la configuración de JWT a la API
        security='Bearer'  # Define que los endpoints por defecto usan el esquema de seguridad JWT
    )

    from.controllers.productos_controller import product_ns

    api.add_namespace(product_ns, path='/product')

    from.controllers.clientes_controller import client_ns

    api.add_namespace(client_ns, path='/client')

    # Retornamos la aplicación ya configurada
    return app
