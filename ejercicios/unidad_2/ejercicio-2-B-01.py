"""

nombre: G
apellido: P
---
Ejercicio: Ejercicio-2-A-01
---
Enunciado:
Crear un programa que pueda sumar los números pares comprendidos entre el 1 y el 10.
"""
total = 0
start = 1
end = 10
for i in range(start,end + 1):
  if i % 2 == 0:
    total = total + (i)
print(f"La suma de los números pares del {start} al {end} es: {total}")



