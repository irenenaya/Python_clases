class TomaInput:
    def __init__(self) -> None:
        self.N = 0
        self.nombre = ''
        self.nombre_usuario = ''

    def tomar_int(self):
        self.N = int(input("Ingrese un numero"))
        

    def tomar_nombre(self):
        self.nombre = input("Ingrese un nombre")
        

    def tomar_input(self): # equivalente a tomar_datos_tablero
        self.tomar_int()
        self.tomar_nombre()
        return self.N, self.nombre

    def tomar_datos_usuario(self):
        #llamar a las funciones que tomen nombre del jugador y nombre del tablero
        # retona estos dos datos
        pass




class Escritor:
    def __init__(self, tablero, dicc, arch) -> None:
        self.tablero = tablero
        self.dicc = dicc
        self.arch = arch
        self.escribir_archivo()
        self.escribir_solucion()



    def escribir_archivo(self):
        # crear archivo usando self.nombre
        # escrbir hileras desde tablero usando self.tablero
        pass

    def escribir_solucion(self):
        pass


class Tablero:
    def __init__(self, N, palabras) -> None:
        self.palabras = palabras
        self.N = N
        self.matriz = 0
        self.diccionario = {}
        self.palabra_actual = ''
        
        

    def generar_tablero(self):
        pass
        # por cada palabra:
            # elijo ubicacion al azar
            # verifico si ubicacion esta OK
            # agrego palabra a matriz
            # agrego palabra a diccionario
        # lleno resto de matriz con letras al azar. 
        # return self.matriz, self.diccionario. 

def main():
    datos = TomaInput()
    N, nombre = datos.tomar_input()

    print (N, nombre)

if __name__ == "__main__":
    main()
