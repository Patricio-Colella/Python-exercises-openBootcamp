import pickle

class Vehiculo:
    ruedas=4
    ventanas=4
    puertas=2
    motor="diesel"
    fuerza=1000,5

    def __str__(self):
        return f"este vehiculo tiene:\n<{self.ruedas} ruedas>\n<{self.ventanas} ventanas>\n<{self.puertas} puertas>\n<{self.fuerza} caballos de fuerza>\n"

auto = Vehiculo()

classHolder = open("classHolder.txt","wb")

pickle.dump(auto,classHolder)

classHolder.close()

classHolder = open("classHolder.txt","rb")
autoCargado = pickle.load(classHolder)

print(autoCargado)
input()
