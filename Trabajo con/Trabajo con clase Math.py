

import math

print("Este programa halla la raiz cuadrada de un numero")

numero = int(input("Introduce un numero: "))

intentos = 1  # inicia en uno porque ya hemos introducido el 1º numero

while numero < 0:  # mientras el numero sea negativo, osea menor a 0
    print("El valor numerico no puede ser negativo")

    numero = int(input("Introduce un numero: "))  # Inntroducimos x segunda vez

          # Aumenta en 1 por cada vuelta que introducimos un negativo

    # si introducimos 5 veces numeros negativos, para(break) el programa
    if intentos == 5:
        break

if intentos == 5:
    print("Lo siento, no puedo realizar el calculo")
else:
    print(math.isqrt(numero))
