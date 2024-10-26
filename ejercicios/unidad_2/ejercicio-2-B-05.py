"""

nombre: G
apellido: P
---
Ejercicio: Ejercicio-2-A-03
---
Enunciado:
Crear un programa que solicite 5 números mediante prompt.
Calcular la suma acumulada y el promedio de los números ingresados
"""
total = 0
for i in range(5):  
  number = int(input("Ingrese numero: "))
  total = total + number
  average = total / 5

print("La suma acumulada es:", total)
print("El promedio es:", average)



