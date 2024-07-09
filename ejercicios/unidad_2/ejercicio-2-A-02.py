"""

nombre: Genaro
apellido: Pennone
---
Ejercicio: Ejercicio-2-A-02
---
Enunciado:
Crear un programa que pida al usuario un número y pueda calcular si es o no mayor de edad.
Si es mayor de 18 se mostrará el mensaje “MAYOR” caso contrario “MENOR”.
"""

number = int(input("Ingrese número: "))
if number >= 18:
  print("MAYOR")
else:
  print("MENOR")



