import json
import os


class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        """Actualiza la cantidad de un producto."""
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        """Actualiza el precio de un producto."""
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    """Clase que maneja la colección de productos en el inventario."""

    def __init__(self, archivo="inventario.json"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        """Agrega un nuevo producto al inventario."""
        self.productos[producto.id_producto] = producto
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad y/o precio de un producto existente."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo JSON."""
        with open(self.archivo, 'w') as f:
            json.dump({id: vars(prod) for id, prod in self.productos.items()}, f)
        print("Inventario guardado correctamente.")

    def cargar_desde_archivo(self):
        """Carga el inventario desde un archivo JSON o lo crea si no existe."""
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                try:
                    data = json.load(f)
                    self.productos = {id: Producto(**prod) for id, prod in data.items()}
                    print("Inventario cargado correctamente.")
                except json.JSONDecodeError:
                    print("El archivo estaba vacío o corrupto, iniciando un inventario nuevo.")
        else:
            with open(self.archivo, 'w') as f:
                json.dump({}, f)
            print("Archivo de inventario creado. Iniciando con inventario vacío.")


def menu():
    """Muestra el menú interactivo del sistema de gestión de inventario."""
    inventario = Inventario()

    while True:
        print("\n=== Sistema de Gestión de Inventario ===")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar inventario")
        print("5. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            inventario.mostrar_productos()
        elif opcion == "5":
            inventario.guardar_en_archivo()
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()

