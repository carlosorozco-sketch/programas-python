# Definición de la clase Engine (Motor)
class Engine:
    # Método para iniciar el motor
    def start(self):
        # Imprime en consola el mensaje que confirma que el motor ha arrancado
        print("Engine started")

# Definición de la clase Car (Automóvil)
class Car:
    # Método constructor que se ejecuta al crear un nuevo objeto Car
    def __init__(self, engine):
        # Asigna el objeto motor recibido como parámetro al atributo propio 'engine' 
        self.engine = engine

    # Método para encender el automóvil
    def start_car(self):
        # Llama al método start() del objeto engine asociado a esta instancia del auto
        self.engine.start()

# --- Ejemplo de uso y prueba del programa ---

# Se crea una objeto de la clase Engine
mi_motor = Engine()

# Se crea una instancia de Car pasando la instancia de Engine creada anteriormente
mi_auto = Car(mi_motor)

# Se manda a llamar el método start_car() para probar su funcionamiento
mi_auto.start_car()