class Producto:
    def __init__(self, id, nombre, cantidad, unidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad} {self.unidad}, Precio por {self.unidad}: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, id, nombre, cantidad, unidad, precio):
        for producto in self.productos:
            if producto.id == id:
                print("Error: El ID ya existe.")
                return
        self.productos.append(Producto(id, nombre, cantidad, unidad, precio))
        print("Producto añadido.")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad, unidad, precio):
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if unidad is not None:
                    producto.unidad = unidad
                if precio is not None:
                    producto.precio = precio
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def main():
    inventario = Inventario()
    while True:
        print("\n1. Añadir producto\n2. Eliminar producto\n3. Actualizar producto\n4. Mostrar productos\n5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            unidad = input("Unidad de medida (libra, quintal, unidad, etc.): ")
            precio = float(input("Precio por unidad de medida: "))
            inventario.añadir_producto(id, nombre, cantidad, unidad, precio)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            unidad = input("Nueva unidad de medida (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio por unidad de medida (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            unidad = unidad if unidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, unidad, precio)

        elif opcion == "4":
            inventario.mostrar_productos()

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
