# # Nombre: Genaro
# # Apellido: Pennone

# # Enunciado:
# De los 3 Jugadores de un Reality Show, se registra:
# nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
# Informar:
# a. nombre del candidato con más votos
# b. nombre y edad del candidato con menos votos
# c. el promedio de edades de los candidatos
# d. total de votos emitidos.
# Todos los datos se ingresan mediante input()



def ingresar_edad():
    edad = int(input("Ingrese Edad (mayor a 25): "))
    while (edad <= 25 or not edad.isnumeric(edad)):
        print("La edad debe ser mayor a 25. Por favor, reingrese")
        edad = int(input("Ingrese Edad (mayor a 25): "))
    return edad

def ingresar_votos():
    votos = int(input("Ingrese Puntos: "))
    while votos < 0 or not votos.isnumeric(votos):
        print("El puntaje no puede ser menor a 0. y solo numeros Reingrese.")
        votos = int(input("Ingrese Puntos: "))
    return votos

contador = 0
players = []

while contador < 3:
    print(f"Jugador {contador + 1}:")
    
    name = input(f"Ingrese Nombre del jugador {contador + 1}: ")
    age = ingresar_edad()  
    points = ingresar_votos()
    
    player_info = {"Nombre": name, "Edad": age, "Puntos": points}
    players.append(player_info)
    
    contador += 1

total_votos = 0
sum_edades = 0
indice_mas_votos = 0
indice_menos_votos = 0

for i in range(len(players)):
    total_votos += players[i]["Puntos"]
    sum_edades += players[i]["Edad"]
    
    if players[i]["Puntos"] > players[indice_mas_votos]["Puntos"]:
        indice_mas_votos = i
    if players[i]["Puntos"] < players[indice_menos_votos]["Puntos"]:
        indice_menos_votos = i

promedio_edades = sum_edades / len(players)

print("\nResultados:")
tide = False
if (players[1]["Puntos"] == players[2]["Puntos"] or
    players[1]["Puntos"] == players[3]["Puntos"] or
    players[2]["Puntos"] == players[3]["Puntos"]):
    tide = True
if tide:
    print("Hay empate de puntos")
    for i in range(len(players)):
        print(f"Nombre:  {players[i]["Nombre"]}")
        print(f"Puntos:  {players[i]["Puntos"]}")

else:
    print(f"Candidato con más votos: {players[indice_mas_votos]['Nombre']}")
    print(f"Candidato con menos votos: {players[indice_menos_votos]['Nombre']}, Edad: {players[indice_menos_votos]['Edad']}")

print(f"Promedio de edades de los candidatos: {promedio_edades:.2}")
print(f"Total de votos emitidos: {total_votos}")
