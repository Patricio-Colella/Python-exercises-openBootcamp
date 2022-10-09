from functools import reduce

def filtrarImpares(x):
    return int(x)%2!=0

lista = input("ingrese lista de numeros(separados por coma):").split(",")

filtered = list(filter(filtrarImpares,lista))

filtered.append(0)

print(reduce(lambda a,b:int(a)+int(b),filtered))

input()
