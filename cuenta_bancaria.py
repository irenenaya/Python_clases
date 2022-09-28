"""
Escribir en Python una clase CuentaBancaria que permita:
Obtener el saldo actual
Depositar dinero
Extraer dinero
Transferir dinero a otra Cuenta Bancaria

¿Qué atributos debe tener la clase?
¿Cuál debe ser la firma de los métodos? (qué recibe y que devuelve cada función)

Tener en cuenta los conceptos antes vistos.
"""

class CuentaBancaria():
    def __init__(self, saldo = 0) -> None:
        self.__saldo = saldo
        self.__LIMITE_DIARIO = 2000
        self.__extraido_hoy = 0
        
    # obtener saldo actual
    def obtener_saldo(self):
        """
        Retorna el saldo actual de la cuenta
        """
        return self.__saldo

    # depositar dinero
    def depositar_dinero(self, dinero):
        """
        toma un monto de dinero como argumento y lo suma al saldo
        """
        self.__saldo += dinero

    # extraer dinero
    def extraer_dinero(self, dinero):
        """
        toma un monto de dinero, y si el saldo es suficiente, lo resta y retorna True
        Si el saldo es insuficiente, retorna false
        """
        if self.__saldo - dinero >= 0:
            self.__saldo -= dinero
            return True
        else:
            print("Saldo insuficiente")
            return False

    # transferir a otra CuentaBancaria
    def transferir(self, dinero, destino):
        """
        Toma un monto de dinero y otra cuenta bancaria y, si el saldo es suficiente
        extrae de esta cuenta y deposita en la otra
        """
        if self.extraer_dinero(dinero):
            destino.depositar_dinero(dinero)

    def __str__(self) -> str:
        return "El saldo de la cuenta es: "+ str(self.__saldo)

    def resetear_extraido(self):
        self.__extraido_hoy = 0

miCuenta = CuentaBancaria()
print(miCuenta)
miCuenta.depositar_dinero(1000)
print(miCuenta)
miCuenta.extraer_dinero(200)
print(miCuenta)
miCuenta.extraer_dinero(1000)
otraCuenta= CuentaBancaria(10000)
print(otraCuenta)
otraCuenta.transferir(2000, miCuenta)
print(otraCuenta)
print(miCuenta)
miCuenta.transferir(3000, otraCuenta)

print(otraCuenta)
print(miCuenta)

# 0
# 1000
# 800
# Insuficiente
# 10000
# 8000
# 2800
# insuficiente
        

