import datetime

class Libro:
    def __init__(self, id_libro, titulo, autor, genero, anio_publicacion):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.disponible = True  # El libro está disponible por defecto

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.anio_publicacion})"


class Usuario:
    def __init__(self, id_usuario, nombre, fecha_registro):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.fecha_registro = fecha_registro
        self.prestamos = []  # Lista de libros prestados

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario}, Registro: {self.fecha_registro})"


class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False

    def devolver_libro(self):
        """Marcar el libro como devuelto"""
        self.devuelto = True
        self.libro.disponible = True
        print(f"El libro '{self.libro.titulo}' ha sido devuelto por {self.usuario.nombre}.")

    def __str__(self):
        return f"Prestamo de '{self.libro.titulo}' a {self.usuario.nombre}, Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con id_libro como clave
        self.usuarios = {}  # Diccionario de usuarios con id_usuario como clave
        self.prestamos = []  # Lista de préstamos realizados

    def agregar_libro(self, libro):
        """Agregar un libro a la biblioteca"""
        self.libros[libro.id_libro] = libro
        print(f"Libro '{libro.titulo}' agregado exitosamente.")

    def agregar_usuario(self, usuario):
        """Agregar un usuario a la biblioteca"""
        self.usuarios[usuario.id_usuario] = usuario
        print(f"Usuario '{usuario.nombre}' registrado exitosamente.")

    def prestar_libro(self, id_usuario, id_libro, dias_prestamo=14):
        """Prestar un libro a un usuario"""
        if id_usuario not in self.usuarios:
            print(f"Error: Usuario con ID {id_usuario} no encontrado.")
            return

        if id_libro not in self.libros:
            print(f"Error: Libro con ID {id_libro} no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[id_libro]

        if not libro.disponible:
            print(f"Error: El libro '{libro.titulo}' no está disponible.")
            return

        fecha_prestamo = datetime.date.today()
        fecha_devolucion = fecha_prestamo + datetime.timedelta(days=dias_prestamo)

        prestamo = Prestamo(usuario, libro, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(prestamo)
        libro.disponible = False
        usuario.prestamos.append(prestamo)

        print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre} hasta el {fecha_devolucion}.")

    def devolver_libro(self, id_usuario, id_libro):
        """Devolver un libro prestado"""
        if id_usuario not in self.usuarios:
            print(f"Error: Usuario con ID {id_usuario} no encontrado.")
            return

        if id_libro not in self.libros:
            print(f"Error: Libro con ID {id_libro} no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[id_libro]

        # Buscar el préstamo correspondiente
        for prestamo in usuario.prestamos:
            if prestamo.libro.id_libro == id_libro and not prestamo.devuelto:
                prestamo.devolver_libro()
                return

        print(f"Error: No se encontró un préstamo activo para el libro '{libro.titulo}' por parte de {usuario.nombre}.")

    def mostrar_libros(self):
        """Mostrar todos los libros disponibles en la biblioteca"""
        print("\nLibros disponibles:")
        for libro in self.libros.values():
            estado = "Disponible" if libro.disponible else "No disponible"
            print(f"{libro.id_libro}. {libro} - {estado}")

    def mostrar_usuarios(self):
        """Mostrar todos los usuarios registrados en la biblioteca"""
        print("\nUsuarios registrados:")
        for usuario in self.usuarios.values():
            print(usuario)

    def mostrar_prestamos(self):
        """Mostrar todos los préstamos realizados"""
        print("\nPréstamos realizados:")
        for prestamo in self.prestamos:
            print(prestamo)

# Función principal de demostración
def main():
    biblioteca = Biblioteca()

    # Agregar libros
    libro1 = Libro(1, "Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 1967)
    libro2 = Libro(2, "1984", "George Orwell", "Distopía", 1949)
    libro3 = Libro(3, "El gran Gatsby", "F. Scott Fitzgerald", "Ficción", 1925)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Agregar usuarios
    usuario1 = Usuario(1, "Ana", datetime.date(2023, 1, 15))
    usuario2 = Usuario(2, "Carlos", datetime.date(2023, 3, 10))
    biblioteca.agregar_usuario(usuario1)
    biblioteca.agregar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro(1, 1, 7)  # Prestar "Cien años de soledad" a Ana
    biblioteca.prestar_libro(2, 2, 14) # Prestar "1984" a Carlos

    # Mostrar estado de la biblioteca
    biblioteca.mostrar_libros()
    biblioteca.mostrar_usuarios()
    biblioteca.mostrar_prestamos()

    # Devolver libro
    biblioteca.devolver_libro(1, 1)  # Ana devuelve "Cien años de soledad"

    # Mostrar estado después de devolución
    biblioteca.mostrar_libros()
    biblioteca.mostrar_prestamos()

if __name__ == "__main__":
    main()
