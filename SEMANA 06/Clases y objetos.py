# Clase base para todos los empleados
class Empleado:
    def __init__(self, nombre, salario):
        # Atributos privados
        self.__nombre = nombre
        self.__salario = salario

    # Métodos para obtener y modificar los atributos
    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_salario(self):
        return self.__salario

    def establecer_salario(self, salario):
        self.__salario = salario

    # Método que debe ser implementado por las subclases
    def calcular_salario(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase")

# Clase para el empleado tipo "Desarrollador"
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguajes_programacion):
        super().__init__(nombre, salario)  # Llamamos al constructor de la clase base
        self.lenguajes_programacion = lenguajes_programacion  # Lista de lenguajes que sabe

    # Implementamos el cálculo del salario para el desarrollador
    def calcular_salario(self):
        # Bonificación por cada lenguaje que sabe
        bono = len(self.lenguajes_programacion) * 100
        return self.obtener_salario() + bono

# Clase para el empleado tipo "Gerente"
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    # Implementamos el cálculo del salario para el gerente
    def calcular_salario(self):
        # Bonificación fija para el gerente
        bono = 800
        return self.obtener_salario() + bono

# Función para mostrar el salario de cualquier tipo de empleado
def mostrar_salario(empleado):
    print(f"El salario de {empleado.obtener_nombre()} es: {empleado.calcular_salario()}")

# Creación de un desarrollador y un gerente
desarrollador = Desarrollador("Ana", 800, ["Python", "Java", "JavaScript"])
gerente = Gerente("Carlos", 1700, "TI")

# Mostrar salarios de ambos empleados
mostrar_salario(desarrollador)  # El salario de Ana es: 800 + 300 = 1100
mostrar_salario(gerente)        # El salario de Carlos es: 1700 + 800 = 2500

# Acceso a métodos para obtener datos específicos
print(f"El nombre del desarrollador es: {desarrollador.obtener_nombre()}")
print(f"El salario del gerente es: {gerente.obtener_salario()}")