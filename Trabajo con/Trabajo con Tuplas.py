

MisDatos = ("Eloy", 16, "septiembre", 1980)

MiCoche = ["peugeot", 2007, "rojo", 1.6, "diesel"]

MiPiso = ("valencia", "puzol", 40, 5, "valencia")


MisDatosLista = list(MisDatos)  # List convierte una Tupla a Lista
print(MisDatosLista)

MiCocheTupla = tuple(MiCoche)  # Tuple convierte una Lista en Tupla
print(MiCocheTupla)

print(40 in MiPiso)  # in pregunta si el elemento esta dentro de la Tupla

# count muestra las veces que esta el elemento en la Tupla
print(MiPiso.count("valencia"))

print(len(MisDatos))#len indica la cantidad de elementos dentro de la Tupla

MiBicicleta=("winora","naranja",2002, 28, 24)

nombre, color, agno, rodado, cambios=MiBicicleta#Desempaquetar Tuplas

print(color)