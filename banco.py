from http import client
from cuenta_bancaria import CuentaBancaria



class Cuenta_Corriente(CuentaBancaria):
    def __init__(self, saldo=0) -> None:
        super().__init__(saldo)

class Caja_Ahorro(CuentaBancaria):
    def __init__(self, saldo=0) -> None:
        super().__init__(saldo)


class Cliente:
    def __init__(self, nombre, edad) -> None:
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

class Banco:
    def __init__(self) -> None:
        self.clientes = []

    def agregar_cliente(self, nombre, edad):
        self.clientes.append(Cliente(nombre, edad))

    def abrir_cuenta_corriente_a_cliente(self, cliente, saldo=0):
        cuenta = Cuenta_Corriente(saldo)
        cliente.abrir_cuenta(cuenta)

    def abrir_caja_ahorro_a_cliente(self, cliente, saldo=0):
        cuenta = Cuenta_Corriente(saldo)
        cliente.abrir_cuenta(cuenta)

