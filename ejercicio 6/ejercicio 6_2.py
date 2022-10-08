class Alumno:
    _nombre=None
    _nota=None
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota

    def new_nota(self,nota):
        self._nota=nota

    def new_nombre(self,nombre):
        self._nombre=nombre

    def nota(self):
        print("su nota es ",self._nota)

    def nombre(self):
        print("su nombre es ",self._nombre)

    def aprobo(self):
        if int(self._nota)>7:
            print("felicidades! la nota "+self._nota+" se considera aprobada!")
        else:
            print("lo sentimos, la nota "+self._nota+" se considera desaprobada")


nombre = input("ingrese nombre:")
nota = input("ingrese nota:")

alumno = Alumno(nombre,nota)

alumno.nombre()
alumno.nota()
print("aprobo?")
alumno.aprobo()
nota = input("ingrese nota de examen nuevo")
alumno.new_nota(nota)
print("aprobo?")
alumno.aprobo()
input()
