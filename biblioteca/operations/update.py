from biblioteca.models.models import Autor, Libro, Usuario, Prestamo


def actualizar_autores(criterio, actualizacion):
    return Autor.objects(**criterio).update(**actualizacion)


def actualizar_libros(criterio, actualizacion):
    return Libro.objects(**criterio).update(**actualizacion)


def actualizar_usuarios(criterio, actualizacion):
    return Usuario.objects(**criterio).update(**actualizacion)


def actualizar_prestamos(criterio, actualizacion):
    return Prestamo.objects(**criterio).update(**actualizacion)
