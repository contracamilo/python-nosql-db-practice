from biblioteca.models.models import Autor, Libro, Usuario, Prestamo


def eliminar_autores(criterio):
    return Autor.objects(**criterio).delete()


def eliminar_libros(criterio):
    return Libro.objects(**criterio).delete()


def eliminar_usuarios(criterio):
    return Usuario.objects(**criterio).delete()


def eliminar_prestamos(criterio):
    return Prestamo.objects(**criterio).delete()
