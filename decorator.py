from abc import ABC, abstractmethod


class Jugador:
    def __init__(self) -> None:
        pass
        
        
    def toma_input(self, c):
        if   c=='w':
            print('hacia adelante')
        elif c == 'a':
            print('hacia izquierda')
        elif c == 's':
            print('hacia atras')
        elif c == 'd':
            print('hacia derecha')
        elif c == 'e':
            print('ataque')
        elif c == ' ':
            print('salto')
        else:
            print('no definido')  

class DecoradorJugador(ABC):
    @abstractmethod
    def toma_input(self, c):
        pass

class JugadorRapido(DecoradorJugador):
    def __init__(self, base) -> None:
        self.base = base

    def toma_input(self, c):
        if c == 'w':
            print("mas rápido", end=' ')

        self.base.toma_input(c)


class JugadorFuego(ABC):
    def __init__(self, base) -> None:
        self.base = base

    def toma_input(self, c):
        if c == 'e':
            print("con fuego ", end=' ')
        self.base.toma_input(c)
    

class JugadorSalto(ABC):
    def __init__(self, base) -> None:
        self.base = base

    def toma_input(self, c):
        if c == ' ':
            print("Doble salto ", end =' ')
        self.base.toma_input(c)


jugador = Jugador()
print('jugador original')
jugador.toma_input('e')
jugador.toma_input(' ')
jugador.toma_input('w')
print('')
jugador = JugadorSalto(jugador)
print('agrego salto')
jugador.toma_input('e')
jugador.toma_input(' ')
jugador.toma_input('w')
print('')
jugador = JugadorFuego(jugador)
print('agrego fuego')
jugador.toma_input('e')
jugador.toma_input(' ')
jugador.toma_input('w')
print('')
jugador = JugadorRapido(jugador)
print('agrego velocidad')
jugador.toma_input('e')
jugador.toma_input(' ')
jugador.toma_input('w')