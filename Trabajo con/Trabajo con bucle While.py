

edad = int(input("introduce tu edad, por favor "))

while edad < 0 or edad > 110:
    print("Has introducido una edad negativa o no valida")
    edad = int(input("introduce tu edad, por favor "))

print("gracias, puedes pasar")
print("La edad del usuario es " + str(edad))
