"""

nombre: G
apellido: P
---
Ejercicio: Ejercicio-2-A-03
---
Enunciado:
Crearun programa que al ingresar un número puede calcular si es mayor, 
niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años) 
adolescente (edad entre 13 y 17 años) de edad.
"""

age = int(input("Ingrese Edad: "))
if age < 0:
  print("Edad Invalida")
else:
  if age < 10:
    print("Es Niño")
  elif  age  < 13:
    print("Es Pre-Adolescente")
  elif age  < 17:
    print("Adolescente")

  else :
    print("Es Mayor")



