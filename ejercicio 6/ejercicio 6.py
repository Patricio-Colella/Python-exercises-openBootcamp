class Vehiculo:
    color=None
    ruedas=None
    puertas=None
    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

class Coche(Vehiculo):
    velocidad=None
    cilindrada=None
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        super().__init__(color,ruedas,puertas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

color=input("color? ")
ruedas=input("ruedas? ")
puertas=input("puertas? ")
velocidad=input("velocidad? ")
cilindrada=input("cilindrada? ")

newCoche = Coche(color,ruedas,puertas,velocidad,cilindrada)

print("newCoche=",newCoche)
print("color=",newCoche.color)
print("ruedas=",newCoche.ruedas)
print("puertas=",newCoche.puertas)
print("velocidad=",newCoche.velocidad)
print("cilindrada=",newCoche.cilindrada)

input()
