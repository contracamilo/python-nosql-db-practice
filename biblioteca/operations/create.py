from biblioteca.models.models import Autor, Libro, Usuario, Prestamo


def insertar_autores(autores_datos):
    autores_objs = [Autor(**autor).save() for autor in autores_datos]
    return autores_objs


def insertar_libros(libros_datos, autores_objs):
    libros_objs = []
    for libro in libros_datos:
        autor_nombre = libro.pop('autor')
        autor_obj = next((autor for autor in autores_objs if autor.nombre == autor_nombre), None)
        if autor_obj:
            libro['autor'] = autor_obj
            libros_objs.append(Libro(**libro).save())
    return libros_objs


def insertar_usuarios(usuarios_datos):
    usuarios_objs = [Usuario(**usuario).save() for usuario in usuarios_datos]
    return usuarios_objs


def insertar_prestamos(prestamos_datos):
    prestamos_objs = []
    for prestamo in prestamos_datos:
        # Obtener los objetos de Usuario y Libro usando los IDs
        usuario_obj = Usuario.objects(id=prestamo['usuario']).first()
        libro_obj = Libro.objects(id=prestamo['libro']).first()

        # Crear un objeto Prestamo con las referencias directas a Usuario y Libro
        if usuario_obj and libro_obj:
            prestamo_obj = Prestamo(usuario=usuario_obj, libro=libro_obj, fecha_prestamo=prestamo['fecha_prestamo'])
            prestamos_objs.append(prestamo_obj.save())

            # Actualizar la lista de libros prestados del usuario
            usuario_obj.libros_prestados.append(libro_obj)
            usuario_obj.save()

    return prestamos_objs
