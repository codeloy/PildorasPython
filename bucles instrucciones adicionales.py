

nombre = "Eloy Arana"

contador = 0

for i in nombre:
    if i == " ":# si i es igual a " " espacio sin caracter
        continue  # con continue decimos que si hay un espacio(" "), que no aumente una vuelta y siga

    contador+=1

print(contador)


class EjemploClase:

    pass # Con pass lo que hacemos es decirle al programa que ignore Ej: class EjemploClase