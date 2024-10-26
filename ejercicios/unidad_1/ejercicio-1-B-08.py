"""

nombre: G
apellido: P
---
Ejercicio: Ejercicio-1-B-08
---
Enunciado:
Cree un programa que permite ingresar el nombre de un producto, el
precio y que calcule el IVA
"""

prod= (input("Ingrese producto:  "))
price = float(input("Ingrese precio $ "))
tax = 0.21
result = price * tax
print(f"El costo del IVA para el producto" ,prod, "es:", result)



