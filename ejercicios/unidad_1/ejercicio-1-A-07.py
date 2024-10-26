"""

nombre: G
apellido: P
---
Ejercicio: Ejercicio-1-A-07
---
Enunciado:
Escribe un programa que muestre por consola el resultado de dividir 10 / 0.
"""
try:
    print("Operacion:", 10, "/", 0)
    value = 10 / 0 # no es posible la divisón por 0 entonces es necesario manejar el error con una excepción
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
