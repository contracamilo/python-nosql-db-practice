from biblioteca.datos import autores_datos, libros_datos, usuarios_datos
from biblioteca.operations.create import insertar_autores, insertar_libros, insertar_usuarios, insertar_prestamos
from biblioteca.operations.read import leer_usuarios, leer_prestamos
from datetime import datetime


if __name__ == '__main__':
    # Insertar datos en las colecciones
    autores_objs = insertar_autores(autores_datos)
    libros_objs = insertar_libros(libros_datos, autores_objs)
    usuarios_objs = insertar_usuarios(usuarios_datos)

    # Obtener los IDs de los usuarios y libros insertados
    usuarios_ids = {usuario.nombre: usuario.id for usuario in usuarios_objs}
    libros_ids = {libro.titulo: libro.id for libro in libros_objs}

    # Crear datos de préstamos utilizando los IDs de usuarios y libros
    prestamos_datos = [
        {"usuario": usuarios_ids["Will Smith"], "libro": libros_ids["Cien Años de Soledad"], "fecha_prestamo": datetime.now(tz=None)},
        {"usuario": usuarios_ids["Emma Johnson"], "libro": libros_ids["1984"], "fecha_prestamo": datetime.now(tz=None)},
    ]

    # Insertar los datos de préstamos
    insertar_prestamos(prestamos_datos)

    # Leer y mostrar los datos actualizados
    print("\nUsuarios actualizados con los libros prestados:")
    for usuario in leer_usuarios():
        print(f"Nombre: {usuario.nombre}, Libros Prestados: {[libro.titulo for libro in usuario.libros_prestados]}")

    print("\nPréstamos en la base de datos:")
    for prestamo in leer_prestamos():
        print(f"Usuario: {prestamo.usuario.nombre}, Libro: {prestamo.libro.titulo}, Fecha de préstamo: {prestamo.fecha_prestamo}")
