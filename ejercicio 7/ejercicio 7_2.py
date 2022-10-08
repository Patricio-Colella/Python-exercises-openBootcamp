import time
import pprint

hora = time.localtime()[3]
res = input("la hora es: "+str(hora)+" es correcto?(ingrese si o la hora correcta):")
if res!="si":
    hora = int(res)

print("hora: ",hora)
if(hora>19):
    print("es hora de ir a casa")
else:
    print("faltan ",19-hora,"hs para ir a casa")

input()
