from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    @abstractmethod
    def consultar_saldo(self):
        pass

    @abstractmethod
    def depositar_dinero(self, dinero):
        pass

    @abstractmethod
    def extraer_dinero(self, dinero):
        pass
    '''
    @abstractmethod
    def depositar_cheque(self, dinero):
        pass
    '''


class CajaAhorro(CuentaBancaria):
    def __init__(self) -> None:
        super().__init__()
        self.saldo = 0

    def consultar_saldo(self):
        return self.saldo

    def depositar_dinero(self, dinero):
        self.saldo += dinero

    def extraer_dinero(self, dinero):
        if self.saldo - dinero >= 0:
            self.saldo -= dinero
            return True
        else:
            print("Saldo insuficiente")
            return False

    def __str__(self) -> str:
        return " El saldo es: " + str(self.saldo)

class CuentaCorriente(CuentaBancaria):
    def __init__(self) -> None:
        super().__init__()
        self.saldo = 0
        self.descubierto =0

    def consultar_saldo(self):
        return self.saldo

    def depositar_dinero(self, dinero):
        self.saldo += dinero

    def extraer_dinero(self, dinero):
        # en descubierto
        if dinero > self.saldo:
            self.descubierto += dinero - self.saldo
            self.saldo = 0
        else:
            self.saldo -= dinero

    def __str__(self) -> str:
        return " El saldo es: " + str(self.saldo) + " y el descubierto es: " + str(self.descubierto)



def fun(cta : CuentaBancaria):
    print(cta)

caja1 = CajaAhorro()
caja1.depositar_dinero(200)
print(caja1)
caja1.extraer_dinero(300)
print(caja1)
caja1.extraer_dinero(100)
print(caja1)

cuenta = CuentaCorriente()
cuenta.depositar_dinero(200)
print(cuenta)
cuenta.extraer_dinero(300)
print(cuenta)

fun(cuenta)
fun(caja1)
fun(42)




