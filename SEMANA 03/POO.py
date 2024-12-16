# Clase para manejar temperaturas
class Clima:
    def __init__(self):
        self.temperaturas = []
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Método para ingresar temperaturas
    def ingresar_temperaturas(self):
        for dia in self.dias:
            temperatura = float(input(f"Ingrese la temperatura del {dia}: "))
            self.temperaturas.append(temperatura)

    # Método para calcular el promedio
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
def main():
    print("Promedio semanal de temperaturas")
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"Temperaturas ingresadas: {clima.temperaturas}")
    print(f"Promedio semanal: {promedio:.2f}°C")

if __name__ == "__main__":
    main()