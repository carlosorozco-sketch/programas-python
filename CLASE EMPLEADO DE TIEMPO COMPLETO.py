# Clase para empleados de tiempo completo
class EmpleadoTiempoCompleto:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def pago(self):
        return self.salario


# Clase para empleados por hora
class EmpleadoPorHora:
    def __init__(self, nombre, horas, tarifa):
        self.nombre = nombre
        self.horas = horas
        self.tarifa = tarifa

    def pago(self):
        return self.horas * self.tarifa


# Clase para empleados de sábado y domingo
class EmpleadoFinDeSemana:
    def __init__(self, nombre, horas, tarifa):
        self.nombre = nombre
        self.horas = horas
        self.tarifa = tarifa

    def pago(self):
        return self.horas * self.tarifa


# Función para calcular el pago
def calcular_pago(empleado):
    print("Empleado:", empleado.nombre)
    print("Pago:", empleado.pago())
    print()


# Crear empleados
empleado1 = EmpleadoTiempoCompleto("Ana", 3000)

empleado2 = EmpleadoPorHora("Carlos", 40, 15)

empleado3 = EmpleadoFinDeSemana("Luis", 16, 20)


# Mostrar información
calcular_pago(empleado1)
calcular_pago(empleado2)
calcular_pago(empleado3)