"""
 Este programa permite ingresar y mostrar información básica de un registro, como nombre, edad, correo, dirección, teléfono y ocupación.
"""


def registrar_usuario():
    """Solicita datos al usuario y devuelve un registro."""
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    correo = input("Ingresa tu correo electrónico: ")
    direccion = input("Ingresa tu dirección: ")
    telefono = input("Ingresa tu número de teléfono: ")
    ocupacion = input("Ingresa tu ocupación: ")

    return {
        "nombre": nombre,
        "edad": edad,
        "correo": correo,
        "direccion": direccion,
        "telefono": telefono,
        "ocupacion": ocupacion
    }


def mostrar_registro(registro):
    """Muestra la información de un registro."""
    print("\n--- Información del Registro ---")
    print(f"Nombre: {registro['nombre']}")
    print(f"Edad: {registro['edad']} años")
    print(f"Correo Electrónico: {registro['correo']}")
    print(f"Dirección: {registro['direccion']}")
    print(f"Teléfono: {registro['telefono']}")
    print(f"Ocupación: {registro['ocupacion']}")


# Flujo principal del programa
print("Gestión de Registro Básico")
registro = registrar_usuario()  # Crear un nuevo registro
mostrar_registro(registro)  # Mostrar el registro
