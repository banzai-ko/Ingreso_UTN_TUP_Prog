"""

nombre: Genaro
apellido: Pennone
---
Ejercicio: Ejercicio-2-A-04
---
Enunciado: Crear un programa que solicite al usuario que ingrese una letra.Se deberá validar que la letra sea  U , T o N (en mayusculas).
En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que la condición se cumpla.
"""

character = input("Ingrese Letra: ")
while character not in ["U", "T", "N"]:
  print("La letra ingresada es:", character)
  character = input("Reingrese Letra: ")

print("La letra ingresada es:", character)


