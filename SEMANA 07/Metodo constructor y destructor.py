# Clase base para el transporte
class Transporte:
    def __init__(self, tipo):
        self.tipo = tipo

    def mostrarInfo(self):
        print(f"Tipo de transporte: {self.tipo}")

    def __del__(self):
        print("Un transporte ha sido eliminado.")


# Transporte urbano
class TransporteUrbano(Transporte):
    def __init__(self, tipo, costo, duracion):
        super().__init__(tipo)
        self.costo = costo
        self.duracion = duracion

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Costo del viaje: ${self.costo:.2f}")
        print(f"Duración del viaje: {self.duracion} minutos")

    def __del__(self):
        print("El transporte urbano ha sido eliminado.")


# Viajes cortos
class ViajeCorto(Transporte):
    def __init__(self, tipo, duracion, costo):
        super().__init__(tipo)
        self.duracion = duracion
        self.costo = costo

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Duración del viaje: {self.duracion} minutos")
        print(f"Costo del viaje: ${self.costo:.2f}")

    def __del__(self):
        print("El viaje corto ha sido eliminado.")


# Viajes largos
class ViajeLargo(Transporte):
    def __init__(self, tipo, ciudad_origen, ciudad_destino):
        super().__init__(tipo)
        self.ciudad_origen = ciudad_origen
        self.ciudad_destino = ciudad_destino
        self.costo, self.duracion = self.calcular_detalles()

    def calcular_detalles(self):
        rutas = {
            ("Quito", "Guayaquil"): (15.00, 8),  # (costo, duración en horas)
            ("Quito", "Lago Agrio"): (16.00, 7),
            ("Quito", "Cuenca"): (12.50, 10),
            ("Quito", "Manta"): (10.00, 8)
        }
        return rutas.get((self.ciudad_origen, self.ciudad_destino), ("Ruta no disponible", "Duración desconocida"))

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Origen: {self.ciudad_origen}")
        print(f"Destino: {self.ciudad_destino}")
        if isinstance(self.costo, float):
            print(f"Costo del viaje: ${self.costo:.2f}")
            print(f"Duración del viaje: {self.duracion} horas")
        else:
            print(self.costo)
            print(self.duracion)

    def __del__(self):
        print("El viaje largo ha sido eliminado.")


# Creación de objetos
print("\nCreando los transportes...")
viajeUrbano = TransporteUrbano("Autobús Urbano", 0.35, 30)
viajeCorto = ViajeCorto("Taxi", 10, 3.50)

# Solicitar datos para el viaje largo
print("\nCreando un viaje largo...")
origen = input("Ingrese la ciudad de origen (e.g., Quito): ")
destino = input("Ingrese la ciudad de destino (e.g., Guayaquil): ")
viajeLargo = ViajeLargo("Autobús Interprovincial", origen, destino)

# Mostrando información
print("\nMostrando los transportes:")
viajeUrbano.mostrarInfo()
print()
viajeCorto.mostrarInfo()
print()
viajeLargo.mostrarInfo()

# Metodo destructor
print("\nOpciones para eliminar:")
print("1. Viaje urbano")
print("2. Viaje corto")
print("3. Viaje largo")
opcion = int(input("Ingrese el número de la opción que desea eliminar: "))

if opcion == 1:
    del viajeUrbano
elif opcion == 2:
    del viajeCorto
elif opcion == 3:
    del viajeLargo
else:
    print("Opción no válida.")

print("\nPrograma terminado.")
