class car:
    """los atributos de clase son el dato general de nuestros 2 tipos de carro
    errores: al intentar definir como poner los atributos marca, color y modelo se notó que iba en instancia"""
    volante = 1
    puertas = 4
    llantas = 4
    faros = 2
    parabrisas = 2
    motor = 1
    velocidades = 6
    ventanas = 6
    retrovisor = 3

    """los atributos instancia especifican la marca, color y modelo para nuestros 2 objetos
    al principio se agregó alrevez el comando e.g. brand = self.brand"""
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

#metodos
    def show_info(self):
        """mostrá toda la informacion de nuestros coches la cada salida de cada uno
        aqui el mayor error fue no pone "f" en print y poner car.brand o car.model, y en el print segundo fue 
         mandar a llamar unicamente a volante sin self."""
        print(f"{self.brand},{self.model},{self.color}")
        print(f""" volante: {self.volante}, puertas: {self.puertas}, llantas: {self.llantas}, faros: {self.faros}, parabrisas: {self.parabrisas}, motor: {self.motor}, velocidades: {self.velocidades}, ventanas: {self.ventanas}, retrovisor: {self.retrovisor}""" )
        print("------------------------------------------")      

"""aqui se comenzó unicamente poniendo car() sin colocar la informacion de adentro"""
car1 = car("chafrolet","corolla","azul")
car1.show_info()


car2 = car("toallota","nubesorb","plateado")
car2.show_info()