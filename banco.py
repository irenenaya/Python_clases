
from cuenta_bancaria import CuentaBancaria



class Cuenta_Corriente(CuentaBancaria):
    def __init__(self, saldo=0) -> None:
        
        super().__init__(saldo)
        self.LIMITE_DIARIO = 10000

class Caja_Ahorro(CuentaBancaria):
    def __init__(self, saldo=0) -> None:
        super().__init__(saldo)


class Cliente:
    def __init__(self, nombre, edad, id) -> None:
        self.nombre = nombre
        self.edad = edad
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def cerrar_cuenta(self, cuenta):
        for i in range (len(self.cuentas)):
            if self.cuentas[i] == cuenta:
                self.cuentas.pop(i)
                break

    def __str__(self) -> str:
        return "El cliente se llama: " + self.nombre + " y tiene " + str(self.edad) + " años"

class Banco:
    def __init__(self) -> None:
        self.clientes = []
        self.dictClientes = {}

    def agregar_cliente(self, nombre, edad, id):
        cliente = Cliente(nombre, edad, id)
        self.clientes.append(cliente)
        self.dictClientes[id] = cliente

    def abrir_cuenta_corriente_a_cliente(self, cliente, saldo=0):
        cuenta = Cuenta_Corriente(saldo)
        cliente.abrir_cuenta(cuenta)

    def abrir_caja_ahorro_a_cliente(self, cliente, saldo=0):
        cuenta = Caja_Ahorro(saldo)
        cliente.abrir_cuenta(cuenta)

banco1 = Banco()

banco1.agregar_cliente("Juan Perez", 30, 123)
banco1.agregar_cliente("Juana Gonzalez", 25 , 456)
print(banco1.dictClientes[123])

banco1.abrir_caja_ahorro_a_cliente(banco1.dictClientes[456])

banco1.clientes[0].id = 333

print(banco1.clientes[0].dni)


