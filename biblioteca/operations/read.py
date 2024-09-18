from biblioteca.models.models import Autor, Libro, Usuario, Prestamo


def leer_autores():
    return Autor.objects()


def leer_libros():
    return Libro.objects()


def leer_usuarios():
    return Usuario.objects()


def leer_prestamos():
    return Prestamo.objects()
