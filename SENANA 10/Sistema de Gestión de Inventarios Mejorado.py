class Producto:
    def __init__(self, id, nombre, cantidad, unidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad} {self.unidad}, Precio: ${self.precio:.2f}"

    def to_line(self):
        """ Convierte un producto a un formato detallado para guardar en el archivo """
        return (f"ID: {self.id}\n"
                f"Nombre: {self.nombre}\n"
                f"Cantidad: {self.cantidad} {self.unidad}\n"
                f"Precio: ${self.precio:.2f}\n"
                "----------------------\n")

    @staticmethod
    def from_lines(lines):
        """ Carga un producto desde líneas de texto """
        try:
            id = lines[0].split(": ")[1].strip()
            nombre = lines[1].split(": ")[1].strip()
            cantidad_unidad = lines[2].split(": ")[1].strip().split()
            cantidad = int(cantidad_unidad[0])
            unidad = " ".join(cantidad_unidad[1:])
            precio = float(lines[3].split(": ")[1].strip().replace("$", ""))
            return Producto(id, nombre, cantidad, unidad, precio)
        except (IndexError, ValueError):
            return None


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """ Carga los productos desde el archivo al iniciar el programa """
        productos = {}
        try:
            with open(self.archivo, "r") as f:
                contenido = f.read().strip().split("\n----------------------\n")
                for bloque in contenido:
                    lineas = bloque.strip().split("\n")
                    producto = Producto.from_lines(lineas)
                    if producto:
                        productos[producto.id] = producto
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
        return productos

    def guardar_inventario(self):
        """ Guarda todos los productos en el archivo con formato detallado """
        with open(self.archivo, "w") as f:
            for producto in self.productos.values():
                f.write(producto.to_line())

    def añadir_producto(self, id, nombre, cantidad, unidad, precio):
        if id in self.productos:
            print("Error: El ID ya existe.")
            return
        self.productos[id] = Producto(id, nombre, cantidad, unidad, precio)
        self.guardar_inventario()
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, unidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
            if unidad is not None:
                producto.unidad = unidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


def main():
    inventario = Inventario()

    while True:
        print("\n1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                unidad = input("Unidad de medida (kg, litro, unidad, etc.): ")
                precio = float(input("Precio por unidad de medida: ").replace("$", ""))
                inventario.añadir_producto(id, nombre, cantidad, unidad, precio)
            except ValueError:
                print("Error: La cantidad y el precio deben ser valores numéricos.")

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            unidad = input("Nueva unidad de medida (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio por unidad de medida (dejar vacío para no cambiar): ")

            cantidad = int(cantidad) if cantidad.strip() else None
            unidad = unidad.strip() if unidad.strip() else None
            precio = float(precio.replace("$", "")) if precio.strip() else None

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
