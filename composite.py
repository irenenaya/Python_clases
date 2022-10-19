from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def retornar_precio(self):
        pass


class Telefono(Item):
    def __init__(self, precio) -> None:
        super().__init__()
        self.__precio = precio

    def retornar_precio(self):
        return self.__precio

class Cargador(Item):
    def __init__(self, precio) -> None:
        super().__init__()
        self.__precio = precio

    def retornar_precio(self):
        return self.__precio

class Auriculares(Item):
    def __init__(self, precio) -> None:
        super().__init__()
        self.__precio = precio

    def retornar_precio(self):
        return self.__precio

class Caja(Item):
    def __init__(self, contenidos) -> None:
        super().__init__()
        self.__contenidos = contenidos

    def retornar_precio(self):
        precio = 0
        for elem in self.__contenidos:
            precio += elem.retornar_precio()
        return precio


caja_telefono_contenido = []
caja_telefono_contenido.append(Telefono(2000))  # 2000
caja_telefono = Caja(caja_telefono_contenido)

cargador_contenido = []
cargador_contenido.append(Cargador(60))  #60
auriculares_contenido = []
auriculares_contenido.append(Auriculares(50))
auriculares_contenido.append(Auriculares(50))  #100
caja_auriculares = Caja(auriculares_contenido)
caja_cargador = Caja(cargador_contenido)

cargador_suelto = Cargador(30) # 30

caja_contenidos = []
caja_contenidos.append(caja_telefono)
caja_contenidos.append(caja_auriculares)
caja_contenidos.append(caja_cargador)
caja_contenidos.append(cargador_suelto)

caja_final = Caja(caja_contenidos)

print(caja_final.retornar_precio())


