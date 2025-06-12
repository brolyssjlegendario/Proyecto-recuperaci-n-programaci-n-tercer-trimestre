from flask_sqlalchemy import SQLAlchemy  # Importa SQLAlchemy, un ORM para gestionar la base de datos en Flask
from flask_login import UserMixin  # Importa UserMixin, que proporciona funciones de autenticación para los usuarios

db = SQLAlchemy()  # Crea una instancia de SQLAlchemy que se conectará con la base de datos

# Definición de la tabla 'User', que almacena los datos de los usuarios
class User(db.Model, UserMixin):  
    id = db.Column(db.Integer, primary_key=True)  # Identificador único de cada usuario (clave primaria)
    username = db.Column(db.String(50), unique=True, nullable=False)  # Nombre de usuario, debe ser único y no puede estar vacío
    password = db.Column(db.String(100), nullable=False)  # Contraseña del usuario, almacenada de manera segura

# Definición de la tabla 'Record', que almacena registros asociados a los usuarios
class Record(db.Model):  
    id = db.Column(db.Integer, primary_key=True)  # Identificador único del registro (clave primaria)
    name = db.Column(db.String(100), nullable=False)  # Nombre del registro, obligatorio
    description = db.Column(db.Text)  # Descripción del registro (puede contener texto largo)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Clave foránea que asocia el registro con un usuario
