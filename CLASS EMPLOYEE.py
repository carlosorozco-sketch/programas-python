class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Llama al constructor de la clase padre (Employee)
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        # Sobrescribe el método para incluir el departamento
        print(f"Name: {self.name}, Salary: ${self.salary}, Department: {self.department}")

# Pruebas de la Actividad 1
empleado = Employee("Ana", 50000)
empleado.show_info()

gerente = Manager("Carlos", 80000, "Ventas")
gerente.show_info()

conserje = Employee("juan",20000)
conserje.show_info()