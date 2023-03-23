
Trabajadores=["Ana", "Maria", "Antonio", "Miguel"]#Esto es una Lista, en otro leguaje sería Array

Trabajadores.append("Juan")#Append agrega un elemento a la Lista

Trabajadores.remove("Miguel")#remove elimina el elemento indicado("Miguel")

DatosTrabajador=["Ana", "Gomez", 1200, True]

print(len(Trabajadores))#Len da la cantidad de elementos dentro de una lista

print(Trabajadores[2])#Imprime la posición nº 2 de la lista, y si usamos negativo imprime de atras hacia delante comenzando por -1 y no por -0. ejemplo: -2 = "Miguel"

print(Trabajadores[0:3])#Esto imprime de la posición 0 a elemento 3 "Antonio"(NO LA POSICION)

del Trabajadores[1]# del elimina el elemento de la pocision elejida, en este caso "Maria"