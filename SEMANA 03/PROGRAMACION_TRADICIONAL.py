# Función para ingresar temperaturas
def ingresar_temperaturas():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []
    for dia in dias:
        temperatura = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    print("Promedio semanal de temperaturas")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"Temperaturas ingresadas: {temperaturas}")
    print(f"Promedio semanal: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
