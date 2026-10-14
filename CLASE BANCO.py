# este programa es de una cuenta de banco y cambia dolares a pesos

class BankAccount:
    # variable del banco
    bank = "Central Bank"

    def __init__(self, saldo):
        self.saldo = saldo

    # metodo para ver el saldo
    def show_balance(self):
        print("Tu saldo es:", self.saldo)

    # metodo de clase para ver el banco
    @classmethod
    def show_bank(cls):
        print("El banco se llama:", cls.bank)

    # metodo estatico para cambiar de dolares a pesos
    @staticmethod
    def convert_currency(value):
        # un dolar vale 18 pesos por ejemplo
        return value * 18.0


# aqui pruebo el codigo
# creo una cuenta con 500 pesos
cuenta1 = BankAccount(500)

# muestro el saldo
cuenta1.show_balance()

# muestro el nombre del banco
BankAccount.show_bank()

# convierto 10 dolares a pesos
pesos = BankAccount.convert_currency(10)
print("10 dolares son:", pesos, "pesos")