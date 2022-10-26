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

    def deshacer(self):
        print ("Deshacer abrir puerta")
        self.receptor.cerrar_puerta()

class ComandoCerrar(Command):
    def __init__(self, receptor) -> None:
        self.receptor = receptor

    def ejecutar(self):
        print ("Comando cerrar puerta")
        self.receptor.cerrar_puerta()

    def deshacer(self):
        print("Deshacer cerrar puerta")
        self.receptor.abrir_puerta()


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

    def invocar_abrir_puerta(self):
        self.abrir.ejecutar()

    def invocar_cerrar_puerta(self):
        self.cerrar.ejecutar()

    def invocar_deshacer_abrir(self):
        self.abrir.deshacer()

    def invocar_deshacer_cerrar(self):
        self.cerrar.deshacer()


inv = Invoker()
inv.invocar_abrir_puerta()
inv.invocar_cerrar_puerta()
inv.invocar_deshacer_abrir()
inv.invocar_deshacer_cerrar()
