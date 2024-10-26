# # Nombre: G
# # Apellido: P

# # Enunciado:
# De los 3 Jugadores de un Reality Show, se registra:
# nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
# Informar:
# a. nombre del candidato con más votos
# b. nombre y edad del candidato con menos votos
# c. el promedio de edades de los candidatos
# d. total de votos emitidos.
# Todos los datos se ingresan mediante input()

cont = 0
edad_total = 0
min_votos = 2 ** 16
max_votos = 0
total_votos = 0
jugadores = 3
edad_minima = 25
while cont < jugadores:
    print(f"JUGADOR {cont + 1}:")
    nombre = input(f"Ingrese Nombre del jugador {cont + 1}: ")
    edad = int(input(f"Ingresa Edad del jugador {cont + 1}: "))
    while edad <= edad_minima:
        edad = int(input(f"Ingresa Edad del jugador {cont + 1}: "))

    edad_total += edad

    votos = int(input(f"Ingresa votos del jugador {cont + 1}: "))
    while votos < 0:
        votos = int(input(f"Ingresa votos del jugador {cont + 1}: "))

    total_votos += votos

    if votos > max_votos:
        max_votos = votos
        mas_votado = nombre

    if votos < min_votos:
        min_votos = votos
        menos_votado = nombre
        menos_votado_edad = edad

    cont += 1

edad_promedio = edad_total / cont

print("\nRESULTADOS:")
print(f"Candidato con más votos: {mas_votado}")
print(f"Candidato con menos votos: {menos_votado} edad: {menos_votado_edad}")
# Ajustamos el formato del promedio
print(f"Promedio de edades de los candidatos: {edad_promedio:.2f}")
print(f"Total de votos emitidos: {total_votos}")
