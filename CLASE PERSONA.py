class person:
    #se decidio no poner atributos de clase porque se vio que no se necesitaban
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.city = location
    #aqui se encuentra el metodo que sera llamado por cada objeto, (el metodo greet), en este codigo no hubo errores de por medio
    def greet(self):
        print(f"Hi, my name is {self.name}, i am {self.age} years old, and i live in {self.city}")
        print("----------------------")

person1 = person("Ana",25,"Mexico")
person1.greet()

person2 = person("Carlos",30,"Colombia")
person2.greet()

person3 = person("Victoria",22,"Ecuador")
person3.greet()
