
paises = {}

pais = input("Introduzca un pais: ")

while pais != "salir":

    ciudad = input("Introduzca una ciudad: ")

    lista_ciudades = paises.setdefault(pais, [ciudad])

    if lista_ciudades != [ciudad]:
        
        paises[pais].append(ciudad)

    pais = input("Introduzca un pais: ")

print(paises)
