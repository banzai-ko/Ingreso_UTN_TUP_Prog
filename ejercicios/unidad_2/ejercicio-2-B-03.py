"""

nombre: Genaro
apellido: Pennone
---
Ejercicio: Ejercicio-2-B-03
---
Enunciado:
Crear un programa que solicite al usuario que ingrese un úmero.
Se deberá validar que se encuentre entre 0 y 9 inclusive. 
En caso no coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla.
"""
start = 0
end = 9
number = int(input(f"Ingrese número entre {start} y {end}: "))

while not number >= start or not number <= end:
  number = int(input(f"Re-ingrese número entre {start} y {end}: "))

print(f"El numero ingresado está en el rango {start}-{end} y es:", number)



