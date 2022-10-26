

class Enemigo:
    __cantidad = 0
    def __init__(self) -> None:
        Enemigo.__cantidad += 1
        self.__id = Enemigo.__cantidad
        
        


    def __str__(self) -> str:
        return "Soy el enemigo número: " + str(self.__id)


    def __del__(self):
        Enemigo.__cantidad -= 1

    def ultimo(self):
        if Enemigo.__cantidad == 1:
            print ("El enemigo número " , self.__id, " es el último que queda")
        else:
            print ("Todavía quedan mas enemigos.")
        

    


enemigos = []
for i in range(5):
    enem = Enemigo()
    enemigos.append(enem)
    print(enem)

for i in range(5):
    enem = enemigos.pop(0)
    enem.ultimo()
    del enem


    