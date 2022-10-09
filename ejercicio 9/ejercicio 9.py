from functools import reduce 


newCountries = set(input("ingrese su lista de paises(separados por coma):").split(","))

hola="hol"

print(f"paises ordenados:{reduce(lambda a,b:a+','+b,sorted(newCountries))}")
input()
