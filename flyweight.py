class Arbol:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        

class FlyweightArbol:
    def __init__(self, imagen) -> None:
        self.imagen = imagen
        self.arboles = []

    def crear_arbol(self, x , y , z):
        #self.arboles.append(Arbol(x, y, z))

        arbol = [a for a in self.arboles if a.x == x and a.y == y and a.z == z]
        if not arbol:
            arbol = Arbol(x, y , z)
            self.arboles.append(arbol)
        else:
            arbol = self.arboles[0]

        return arbol
