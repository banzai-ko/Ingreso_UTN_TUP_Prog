"""

nombre: Genaro
apellido: Pennone
---
Ejercicio: Ejercicio-1-A-11
---
Enunciado:
Crear un programa (suma, resta, multiplicación, y división),
se deberá generar dos variables del tipo “var_a” y “var_b”, asignarles un valor del tipo número a cada una de ellas.
El programa deberá mostrar por consola el resultado de realizar las 4 operaciones aritméticas mencionadas entre ellas
"""

var_a = int(input("Ingrese valor de la variable A: "))
var_b = int(input("Ingrese valor de la variable B: "))
print("Operacion:", "A", "+", "B")
addition = var_a + var_b
print("Resultado suma:", addition)
substract = var_a - var_b
print("Resultado resta:", substract)
mult = var_a * var_b
print("Resultado Multiplicación:", mult)
div = var_a / var_b
print("Resultado División:", div)
