"""

nombre: G
apellido: P
---
Ejercicio: Ejercicio-1-B-04
---
Enunciado:
Cree un programa que pida el nombre,número de comisión, asignatura, docente y si el usuario estuvo presente,
 luego que muestre los datos por consola con las leyendas pertinentes
"""

name = input("Ingrese nombre:  ")
division = input("Ingrese comisión:  ")
signature = input("Ingrese asignatura:  ")
profesor = input("Ingrese docente:  ")
is_present = input("¿Estuvo presente? (S/N):  ").strip().upper() == 'S'
print("Nombre", name)
print("Comisión:", division)
print("Asignatura:", signature)
print("Docente:", profesor)
response = 'sí' if is_present else 'no'
print(f"Presente: {response}")



