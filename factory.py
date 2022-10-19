from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass


class Cuadrado(Forma):
    def __init__(self, lado) -> None:
        super().__init__()
        self.lado = lado

    def calcular_area(self):
        return  self.lado * self.lado

    def calcular_perimetro(self):
        return self.lado * 4

class Rectangulo(Forma):
    def __init__(self, ancho, alto) -> None:
        super().__init__()
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return self.ancho * 2 + self.alto * 2

class Circulo(Forma):
    def __init__(self, radio) -> None:
        super().__init__()
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio * self.radio

    def calcular_perimetro(self):
        return 3.14 * self.radio * 2


class FabricaFormas:
    def crear_formas(self, nombre):
        if nombre == "circulo":
            radio = input("Ingrese el radio del circulo:")
            return Circulo(float(radio))

        if nombre == "cuadrado":
            lado = input("Ingrese el tamaño del lado del cuadrado: ")
            return Cuadrado(float(lado))

        if nombre == "rectangulo":
            ancho = input ("Ingrese el ancho del rectangulo: ")
            alto = input("Ingrese el alto del rectangulo: ")
            return Rectangulo(float(ancho), float(alto))


forma_fabrica = FabricaFormas()
forma = input("Ingrese la forma que desea crear: ")
f = forma_fabrica.crear_formas(forma)
print(f.calcular_area())
