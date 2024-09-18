import os
import mongoengine as me
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env si existe
load_dotenv()


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Creamos una nueva instancia
            cls._instance = super(Database, cls).__new__(cls)
            # Obtener la URI desde las variables de entorno
            uri = os.getenv('MONGODB_URI')
            if not uri:
                raise ValueError("La variable de entorno MONGODB_URI no está definida")
            # Conexión a MongoDB Atlas
            me.connect(host=uri, db='Biblioteca')
        return cls._instance
