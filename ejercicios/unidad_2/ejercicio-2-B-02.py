"""

nombre: Genaro
apellido: Pennone
---
Ejercicio: Ejercicio-2-A-02
---
Enunciado:
Crear un programa que solicite al usuario que ingrese una contraseña mediante prompt
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volver a solicitarla hasta que coincidan.
"""
def validate_password(password): ## Ignorar esta función no corresponde al enunciado
    if len(password) < 10:
        print("La contraseña debe tener al menos 10 caracteres.")
        return False
    elif not any(char.isupper() for char in password):  # Mayus
        print("La contraseña debe tener por lo menos una mayúscula.")
        return False
        #Simbol- Ignorar sobre todo esto
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"
    if not any(char in special_characters for char in password):
        print("La contraseña debe tener por lo menos un símbolo.")
        return False

        print("La contraseña debe tener por lo menos un símbolo.")
        return False
    # print("La contraseña debe tener: ")
    # print("Al menos 10 caracteres")
    # print("Por lo menos 1 mayúscula")
    # print("Por lo menos 1 símbolo")    
    return True

def password_check(password):
    if password == "utn750":
        return True
    else:
        return False

password_match = False

password = input("Ingrese contraseña: ")

while not password_check(password):
    print("Contraseña incorrecta. Reintente.")
    password = input("Ingrese contraseña: ")

print("La contraseña es correcta.")





