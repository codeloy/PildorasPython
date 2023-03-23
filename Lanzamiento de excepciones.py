import math


def calcularRaizCuadrada(numero):

    if numero < 0:

        raise ValueError("El numero no puede ser menor a 0")

    else:

        return math.sqrt(numero)


numeroUsuario = int(input("Introduce un numero: "))

try:
    print(calcularRaizCuadrada(numeroUsuario))
except ValueError:
    print("Error de numero negativo")

print("Por aqui continuaria el programa ")
