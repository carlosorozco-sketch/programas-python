class Accountant:
    def generate_report(self):
        print("Generating financial report")

class Technician:
    def repair_machine(self):
        print("Repairing machine")

class Boss(Accountant, Technician):
    # La clase hereda de ambas y no necesita implementación adicional
    pass

# Pruebas de la Actividad 2
jefe = Boss()

# El objeto Boss puede llamar a los métodos de ambas clases padre
jefe.generate_report()
jefe.repair_machine()