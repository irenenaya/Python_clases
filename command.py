from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

class ComandoAbrir(Command):
    def __init__(self, receptor) -> None:
        self.receptor = receptor

    def ejecutar(self):
        print ("Comando abrir puerta")
        self.receptor.abrir_puerta()

class ComandoCerrar(Command):
    def __init__(self, receptor) -> None:
        self.receptor = receptor

    def ejecutar(self):
        print ("Comando cerrar puerta")
        self.receptor.cerrar_puerta()


class Receptor:

    def abrir_puerta(self):
        print ('abro puerta')
    
    def cerrar_puerta(self):
        print ("cierro puerta")


class Invoker:
    def __init__(self) -> None:
        self.receptor = Receptor()
        self.abrir = ComandoAbrir(self.receptor)
        self.cerrar = ComandoCerrar(self.receptor)
