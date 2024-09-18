import mongoengine as me

from biblioteca.db.db import Database

Database()


# Modelo de Autor
class Autor(me.Document):
    nombre = me.StringField(required=True, max_length=200)
    fecha_nacimiento = me.DateField()
    obras = me.ListField(me.StringField())
    meta = {'collection': 'autores'}


# Modelo de Libro
class Libro(me.Document):
    titulo = me.StringField(required=True, max_length=200)
    autor = me.ReferenceField(Autor, required=True)  # Referencia al modelo Autor
    genero = me.StringField(max_length=100)
    disponibilidad = me.BooleanField(default=True)
    meta = {'collection': 'libros'}


# Modelo de Usuario
class Usuario(me.Document):
    nombre = me.StringField(required=True, max_length=200)
    correo = me.EmailField(required=True)
    libros_prestados = me.ListField(me.ReferenceField(Libro))
    meta = {'collection': 'usuarios'}


# Modelo de Prestamo
class Prestamo(me.Document):
    usuario = me.ReferenceField(Usuario, required=True)  # Referencia al modelo Usuario
    libro = me.ReferenceField(Libro, required=True)  # Referencia al modelo Libro
    fecha_prestamo = me.DateField(required=True)
    meta = {'collection': 'prestamos'}
