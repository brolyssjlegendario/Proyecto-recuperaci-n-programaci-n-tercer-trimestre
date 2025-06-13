import os  # Importa el módulo 'os', que permite interactuar con el sistema operativo


class Config:  # Define una clase de configuración para la aplicación Flask
    SECRET_KEY = 'clave_secreta'  
    # Establece una clave secreta para la aplicación. 
    # Se usa para la seguridad de sesiones, formularios y autenticación.

    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  
    # Define la URL de conexión a la base de datos SQLite.
    # Aquí, 'sqlite:///' indica que se usará SQLite y 'database.db' es el nombre del archivo de la base de datos.

    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    # Desactiva el seguimiento de modificaciones de objetos en SQLAlchemy para mejorar el rendimiento.
