

def comparaListas(lista1, lista2):

    if (len(lista1) != len(lista2)):# si largo de lista1 no es igual a lista2
        return False

    else:

        for i in range(0, len(lista1)):# recorre la lista 1 porque sabemos que son iguales
            if (lista1[i] != lista2[i]):# chequea que cada elemento(i) de lista1 es = a lista2
                return False

    return True


alumnosA = ["Juan", "Pedro", "Ana"]

alumnosB = ["Juan", "Pedro", "Ana"]

print(comparaListas(alumnosA, alumnosB))
