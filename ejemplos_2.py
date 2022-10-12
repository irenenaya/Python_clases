from ejemplos import TomaInput



class Juego:
    def __init__(self, nombre, tablero) -> None:
        self.__nombre = nombre # podria no ser atributo
        self.__nombre_tablero = tablero # podria no ser atributo
        self.__jugador = Jugador(nombre)
        self.__tablero = Tablero(tablero)

        
    def jugar(self):
        # ciclo continua hasta que esten todas las palabras o se ingrese 'fin'
            # imprimir Tablero
            # tomar palabra del usuario. (tomar directamente o agregar funcion a TomaInput())
                # si la palabra está en el tablero:
                    # imprimir mensaje -> esta clase
                    # aumentar puntaje a Jugador -> Jugador
                    # pasar la palabra a mayúscula -> Tablero
                    # agregar la palabra a lista de palabras encontradas -> Tablero
                # si la palabra no está en el tablero:
                    # imprimimos mensaje

        # Imprimir nombre y puntaje del Jugador. (print(self.jugador))
        # Mostrar palabras encontradas en orden. -> Tablero
        # Mostrar palabras no encontradas -> Tablero
        pass



class Jugador:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__puntaje = 0

    # funcion para aumentar puntaje

    # funcion para imprimir resultados (puede ser __str__)

class Tablero:
    def __init__(self, archivo) -> None:
        self.__matriz = 0 # crean a partir de abrir el archivo_tablero
        self.__diccionario = {} # crean a partir de abrir archivo_solucion
        self.__palabras_encontradas = []
        self.abrir_archivo_tablero(archivo)

    def abrir_archivo_tablero(self, archivo):
        # 1) abren el archivo y lo retornan. 
        # 2) abren el archivo y lo guardan en self.matriz
        pass

    # funcion para abrir archivo_solucion

    # funcion que imprima el tablero 

    # funcion que verifique si la palabra esta en el tablero. 

    # funcion para pasar la palabra a mayusculas

    # funcion para agregar la palabra encontrada a palabras_encontradas

    # funcion que retorne self.__palabras_encontradas. O funcion que las imprima. 

    # funcion que o retorne o imprima las palabras no encontradas en orden alfabetico. 

def main():
    datos = TomaInput()
    nombre, tablero = datos.tomar_datos_usuario()
    juego = Juego(nombre, tablero)
    juego.jugar()
    mi_booleano_horrible = juego.getTablero().getMatriz()[0][0].isalpha()