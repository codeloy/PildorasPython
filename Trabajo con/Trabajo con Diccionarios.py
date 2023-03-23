

CapitalesDelMundo = {"España": "Madrid",
                     "Francia": "Toulousse", "Reino Unido": "Londres"}


# Agrega una Clave y un Valor al diccionario
CapitalesDelMundo["Colombia"] = "Bogota"

CapitalesDelMundo["Francia"] = "Paris"  # Cambia un Valor del Diccionario

print(CapitalesDelMundo)

del CapitalesDelMundo["Reino Unido"]  # Borra una Clave del Diccionario

print(CapitalesDelMundo)

# LISTA DENTRO DE UN DICCIONARIO
ClaveCapitales = ["España", "Argentina", "Portugal", "Francia"]

CapitalesPais = {ClaveCapitales[0]: "Madrid", ClaveCapitales[1]
    : "Buenos Aires", ClaveCapitales[2]: "Lisboa", ClaveCapitales[3]: "Paris"}

print(CapitalesPais)

print(CapitalesPais.keys())  # Keys nos da todas las Claves del Diccionario

# Values nos da todos los Valores del Diccionario
print(CapitalesPais.values())

# Len nos da la cantidad de elementos(4) del Diccionario
print(len(CapitalesPais))

# Diccionario dentro de Diccionario

DatosJordan={23:"Jordan", "Nombre":"Michael", "Equipo":"C Bulls", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

print(DatosJordan.keys())#Imprime las Claves o Keys

print(DatosJordan["Anillos"])#Imprime el contenido del Diccionario Anillos

print(DatosJordan)


