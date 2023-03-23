

import random

numero = int(input("introduce un numero del 1 al 100 "))

intentos = 1

numAleatorio = random.randint(1, 100)

while numero != numAleatorio:

    if (numero > numAleatorio):
        print("El numero aleatorio es Menor ")

    if (numero < numAleatorio):
        print("El numero aleatorio es Mayor ")

    numero = int(input("introduce un numero del 1 al 100 "))

    intentos = intentos+1

print("correcto. Has consumido " + str(intentos) + " intentos")
