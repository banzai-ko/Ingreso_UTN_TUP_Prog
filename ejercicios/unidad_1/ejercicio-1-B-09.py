"""

nombre: Genaro
apellido: Pennone
---
Ejercicio: Ejercicio-1-B-09
---
Enunciado:
cree un programa que calcule el promedio de un alumno, ingresando su
nombre apellido, 3 notas, que muestre al final las leyendas pertinentes
"""
name = input("Ingrese nombre:  ")
lastname = input("Ingrese apellido:  ")
grade_a = float(input("Ingrese Nota 1: "))
grade_b = float(input("Ingrese Nota 2: "))
grade_c = float(input("Ingrese Nota 3: "))
average = (grade_a + grade_b + grade_c) / 3
print("Nombre completo", name, lastname)
print(f"Promedio: {average:.2f}")




