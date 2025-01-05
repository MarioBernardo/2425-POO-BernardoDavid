# Definir la clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.cantidad = cantidad  # Cantidad disponible en stock

    # Método para actualizar el stock
    def actualizar_stock(self, cantidad_comprada):
        self.cantidad -= cantidad_comprada  # Restar la cantidad comprada al stock

    # Método para mostrar información del producto
    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Stock: {self.cantidad}"


# Definir la clase Cliente
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre  # Nombre del cliente
        self.email = email    # Correo electrónico del cliente

    # Método para mostrar información del cliente
    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"


# Definir la clase Orden
class Orden:
    def __init__(self, cliente):
        self.cliente = cliente  # El cliente que hizo la compra
        self.productos = []  # Lista de productos que el cliente ha agregado
        self.total = 0  # Total de la compra

    # Método para agregar productos a la orden
    def agregar_producto(self, producto, cantidad):
        if producto.cantidad >= cantidad:  # Verificar si hay suficiente stock
            self.productos.append((producto, cantidad))  # Agregar el producto a la orden
            producto.actualizar_stock(cantidad)  # Actualizar el stock
            self.total += producto.precio * cantidad  # Sumar al total de la compra
            print(f"{producto.nombre} agregado a la orden.")
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    # Método para mostrar la orden final
    def mostrar_orden(self):
        print(f"Orden de {self.cliente.nombre}:")
        for producto, cantidad in self.productos:
            print(f"{producto.nombre} - {cantidad} unidades")
        print(f"Total: ${self.total}")


# Crear algunos productos con los nuevos precios
producto1 = Producto("Camiseta Adulto BSC 2025", 69.90, 100)  # Camiseta para adulto
producto2 = Producto("Camiseta Niños BSC 2025", 69.90, 50)    # Camiseta para niños
producto3 = Producto("Pupos Nike Talla 40", 100, 30)          # Pupos marca Nike

# Crear un cliente
cliente1 = Cliente("David Bernardo", "david@ejemplo.com")

# Crear una orden para el cliente
orden_cliente1 = Orden(cliente1)

# Agregar productos a la orden
orden_cliente1.agregar_producto(producto1, 2)  # David compra 2 camisetas para adulto
orden_cliente1.agregar_producto(producto2, 2)  # David compra 2 camiseta para niño
orden_cliente1.agregar_producto(producto3, 1)  # David compra 1 par de pupos

# Mostrar la orden final
orden_cliente1.mostrar_orden()