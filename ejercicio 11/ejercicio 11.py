import sqlite3
import pprint



alumns = []
while len(alumns) < 8:
    print("<alumno "+str(len(alumns)+1)+">(de 8)")
    newAlumno = (input("-nombre:"),input("-apellido:"))
    
    alumns.append(newAlumno)

conn = sqlite3.connect("ejercicio_11.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM 'Alumnos'")
cursor.close()

i=0
while i<len(alumns):
    cursor = conn.cursor()
    name = alumns[i][0]
    surname = alumns[i][1]
    cursor.execute(f"INSERT INTO 'Alumnos' (id,nombre,apellido) VALUES ('{i+1}','{name}','{surname}')")
    cursor.close()
    i+=1

conn.commit()
conn.close()

conn = sqlite3.connect("ejercicio_11.db")
cursor = conn.cursor()
rows = cursor.execute(f"SELECT * FROM 'Alumnos'")

for row in rows:
    print("alumno nº:"+str(row[0]))
    print("nombre completo:"+row[1]+" "+row[2])
    print("<------------------------------------------------------------>")

cursor.close()

founded = False

while founded==False:
    
    searchName = input("ingrese el nombre que busca:")

    cursor = conn.cursor()

    query = f'SELECT * FROM "Alumnos" WHERE nombre="{searchName}"'
    
    row = cursor.execute(query)
    data=row.fetchone()
    cursor.close()
    
    if data == None:
        print("alumno no encontrado, intente nuevamente")
        continue

    founded=True

    print(data)
    
    
    
conn.close()
input()

