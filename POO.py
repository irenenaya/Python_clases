class Vehiculo:
    def __init__(self, marca, modelo, anio) -> None:
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = 0
        self.motor = Motor(10)
        self.pasajeros = []

    def acelerar(self, velocidad):
        print(" Clase base ")

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

    


class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas) -> None:
        super().__init__(marca, modelo, anio)
        self.puertas = puertas
        
    def __str__(self) -> str:
        #return "La marca es: " + self.marca + " y tiene " + str(self.puertas) + " puertas" + " La velocidad es: " + str(self.velocidad)
        ret = ''
        for p in self.pasajeros:
            ret += p.nombre
        return "Pasajeros: " + ret
    def acelerar(self, velocidad):
        if not self.motor.encendido:
            self.motor.encender()
        if (self.velocidad + velocidad <= 180):
            self.velocidad += velocidad
        else:
            self.velocidad = 180
        print(self.motor)


class Avion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad) -> None:
        super().__init__(marca, modelo, anio)
        self.capacidad = capacidad

    def __str__(self) -> str:
        #return "La marca es: " + self.marca +  " y lleva " + str(self.capacidad) + " pasajeros" + " La velocidad es: " + str(self.velocidad)
        ret = ''
        for p in self.pasajeros:
            ret += p.nombre
        return "Pasajeros: " + ret
    def acelerar(self, velocidad):
        if not self.motor.encendido:
            self.motor.encender()
        if (self.velocidad + velocidad <= 1000):
            self.velocidad += velocidad
        else:
            self.velocidad = 1000
        print(self.motor)


class Motor:
    def __init__(self, cil) -> None:
        self.cilindrada = cil
        self.encendido = False

    def encender(self):
        self.encendido = True

    def __str__(self) -> str:
        ret = ''
        if self.encendido:
            ret = ". Está encendido"
        else:
            ret = ". No está encendido"
        return "El motor tiene: " + str(self.cilindrada) + ret

    
class Pasajero:
    def __init__(self, nom) -> None:
        self.nombre = nom

    def __str__(self) -> str:
        return self.nombre + " "


miAuto = Auto("Peugeot", "", 2010, 4)

miAvion = Avion("Cessna", "", 2000, 200)

p1 = Pasajero("Maité")
p2 = Pasajero("Sebastián")
p3 = Pasajero("Valentino")
p4 = Pasajero("Irene")
# vector<Vehiculo> misVehiculos;
# 

miAuto.agregar_pasajero(p1)
miAuto.agregar_pasajero(p2)

miAvion.agregar_pasajero(p3)
miAvion.agregar_pasajero(p4)

l = [miAuto, miAvion]

for elem in l:
    elem.acelerar(1000)
    print(elem)


