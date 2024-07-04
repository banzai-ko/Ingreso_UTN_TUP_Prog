import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nicolas Busti
DNI: 40.238.844


Nos encargan el desarrollo de una aplicación que le permita a sus usuarios inscribirse a un listado de viajeros:

A) Para ello deberás programar el botón  para poder cargar los siguientes datos de 5 personas:
    * Nombre
    * Altura (entre 60 cm y 200 cm)
    * Peso (entre 40 kilos y 250 kilos)
    * Edad (entre 1 y 100 )



B) Al presionar el botón mostrar se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal)

Del punto C solo deberá realizar 2 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:

    Informe 1- Tome el último número de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- el promedio de altura entre todos los usuarios ingresados que sean mayores de 18 años


     Realizar los informes correspondientes a los números obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR.
C)
    #! 0)
        A- El nombre de la persona con el menor peso ingresado
        B- La cantidad de personas de más de 50 años
    #! 1)
        A- El nombre de la persona con el mayor peso ingresado
        B- La cantidad de personas de menos de 50 años
    #! 2)
        A- El nombre de la persona con la mayor altura ingresada
        B- La cantidad de personas de más de 80 kilos
    #! 3)
        A- El nombre de la persona con la menor altura ingresada
        B- La cantidad de personas de menos de 100 kilos
    #! 4)
        A- El nombre de la persona con la mayor edad ingresada
        B- La cantidad de personas de más de 100 cm de altura
    #! 5)
        A- El nombre de la persona con la menor edad ingresada
        B- La cantidad de personas de menos de 170 cm de altura
    #! 6)
        A- El nombre de la persona con la mayor edad ingresada
        B- La cantidad de personas de menos de 160 cm de altura
    #! 7)
        A- El nombre de la persona con la menor altura ingresada
        B- La cantidad de personas de menos de 80 kilos
    #! 8)
        A- El nombre de la persona con el mayor peso ingresado
        B- La cantidad de personas de más  de 50 kilos
    #! 9)
        A- El nombre de la persona con el menor peso ingresado
        B- La cantidad de personas de menos de 18 años

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)


        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Pokedex", command=self.btn_mostrar_pokedex_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Cargar aca los pokemones
        self.lista_nombre = ['Gianni','Octavio','Nicolas','Susana','Capri']
        self.lista_altura = [171,162,158,180,80]
        self.lista_peso = [83,79,43,65,52]
        self.lista_edad = [32,23,26,53,8]

    def btn_mostrar_pokedex_on_click(self):
        nombre_max = None
        edad_max = None
        altura_100 = 0
        mayor_18 = 0
        Suma_edad = 0

        for indice in range(5):

            #Informe 1:
            #! 4) A- El nombre de la persona con la mayor edad ingresada
            if edad_max == None or edad_max < self.lista_edad[indice]:
                edad_max = self.lista_edad[indice]
                nombre_max = self.lista_nombre[indice]


            #B- La cantidad de personas de más de 100 cm de altura

            if self.lista_altura[indice] > 100:
                altura_100 += 1

            #Informe 2- el promedio de altura entre todos los usuarios ingresados que sean mayores de 18 años

            if self.lista_edad[indice] > 18:
                mayor_18 += 1
                Suma_edad = Suma_edad + self.lista_altura[indice]

        promedio = Suma_edad / mayor_18

        print(f'El viajero {self.lista_nombre[indice]} tiene una altura de {self.lista_altura[indice]} un peso de {self.lista_peso[indice]} y una edad de {self.lista_edad[indice]}')
        print(f'La persona con mas edad es {nombre_max} con una edad de {edad_max}')
        print(f'Hay un total de {altura_100} personas mayores a 100cm de altura')
        print(f'El promedio de altura entre los mayores de 18 años es de {promedio}')




    def btn_cargar_pokedex_on_click(self):
        #A) Para ello deberás programar el botón  para poder cargar los siguientes datos de 5 personas:
        #* Nombre
        #* Altura (entre 60 cm y 200 cm)
        #* Peso (entre 40 kilos y 250 kilos)
        #* Edad (entre 1 y 100 )
        for indice in range(5):

            nombre = prompt('Ingrese nombre','Ingrese el nombre del viajero')
            self.lista_nombre.append(nombre)

            altura = int(prompt('Ingrese Altura','Ingrese la Altura del viajero'))
            while altura < 60 or altura > 200:
                altura = int(prompt('ERROR','Ingrese la Altura del viajero'))
            self.lista_altura.append(altura)

            peso = int(prompt('Ingrese peso','Ingrese el peso del viajero'))
            while peso < 40 or peso > 250:
                peso = int(prompt('ERROR','Ingrese el peso del viajero'))
            self.lista_peso.append(peso)

            edad = int(prompt('Ingrese edad','Ingrese la edad del viajero'))
            while edad < 1 or edad > 100:
                edad = int(prompt('ERROR','Ingrese la edad del viajero'))
            self.lista_edad.append(edad)


if __name__ == "__main__":
    app = App()
    app.mainloop()
