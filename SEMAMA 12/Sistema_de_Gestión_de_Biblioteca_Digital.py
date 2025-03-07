class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.categoria} - ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def listar_libros_prestados(self):
        return "\n".join(str(libro) for libro in self.libros_prestados) if self.libros_prestados else "No ha prestado libros."

    def __str__(self):
        return f"Usuario: {self.nombre} - ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.cargar_libros_iniciales()

    def cargar_libros_iniciales(self):
        libros_iniciales = [
            ("El Quijote", "Miguel de Cervantes", "Novela", "123456"),
            ("Cien años de soledad", "Gabriel García Márquez", "Novela", "654321"),
            ("El principito", "Antoine de Saint-Exupéry", "Ficción", "987654"),
            ("1984", "George Orwell", "Ciencia Ficción", "111222"),
            ("Moby Dick", "Herman Melville", "Aventura", "333444"),
            ("Orgullo y prejuicio", "Jane Austen", "Romance", "555666"),
            ("Crimen y castigo", "Fiódor Dostoyevski", "Drama", "777888"),
            ("Los miserables", "Victor Hugo", "Drama", "999000")
        ]
        for titulo, autor, categoria, isbn in libros_iniciales:
            self.libros[isbn] = Libro(titulo, autor, categoria, isbn)

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        self.libros.pop(isbn, None)

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario

    def dar_baja_usuario(self, id_usuario):
        self.usuarios.pop(id_usuario, None)

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)
        if libro and usuario:
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        if usuario:
            libro = usuario.devolver_libro(isbn)
            if libro:
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no registrado.")

    def buscar_libro(self, criterio, valor):
        encontrados = [str(libro) for libro in self.libros.values() if getattr(libro, criterio, "").lower() == valor.lower()]
        return "\n".join(encontrados) if encontrados else "No se encontraron libros."

    def listar_libros_prestados(self, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        return usuario.listar_libros_prestados() if usuario else "Usuario no registrado."


def menu():
    biblioteca = Biblioteca()
    while True:
        print("\nSistema de Gestión de Biblioteca Digital")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.agregar_libro(Libro(
                input("Título: "),
                input("Autor: "),
                input("Categoría: "),
                input("ISBN: ")
            ))
        elif opcion == "2":
            biblioteca.quitar_libro(input("ISBN del libro a quitar: "))
        elif opcion == "3":
            biblioteca.registrar_usuario(Usuario(input("Nombre: "), int(input("ID: "))))
        elif opcion == "4":
            biblioteca.dar_baja_usuario(int(input("ID del usuario a dar de baja: ")))
        elif opcion == "5":
            biblioteca.prestar_libro(input("ISBN: "), int(input("ID Usuario: ")))
        elif opcion == "6":
            biblioteca.devolver_libro(input("ISBN: "), int(input("ID Usuario: ")))
        elif opcion == "7":
            print(biblioteca.buscar_libro(input("Criterio (titulo, autor, categoria): "), input("Valor: ")))
        elif opcion == "8":
            print(biblioteca.listar_libros_prestados(int(input("ID Usuario: "))))
        elif opcion == "9":
            print("Saliendo..."); break
        else:
            print("Opción no válida.")

menu()

