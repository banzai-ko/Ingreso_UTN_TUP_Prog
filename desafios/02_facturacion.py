# Nombre: Genaro
# Apellido: Pennone

# Enunciado:
# Para el departamento de facturación:
# A. Ingresar tres precios de productos y mostrar la suma de los mismos.
# B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
# C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

print("Ingresar Precios")
coke = int(input("Nuka Cola: $"))
branca = int(input("Fernet Branca: $"))
water = int(input("Agua: $"))
subtotal = coke + branca + water
average = ( coke + branca + water ) / 3
total = subtotal * 1.21
print("Subtotal:",  subtotal)
print(f"Promedio:, {average:.2f}")
print(f"Total: {total:.2f}")

