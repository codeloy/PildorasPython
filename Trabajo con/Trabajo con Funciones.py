

# def ImprimeMensajes():#Esta es la declaracion de la Funcion

#     print("Ejemplo numero 1")
#     print("Ejemplo numero 2")
#     print("Ejemplo numero 3")
#     print("Ejemplo numero 4 y ultimo")


# print("El programa ha terminado la ejecucion")

# ImprimeMensajes()#Esta es la llamada a la Funcion

def imprimeMensajes():
    return "Este es el mensaje de la funcion"

valorMensaje = imprimeMensajes()
print(valorMensaje)


# def imprimeMensajePersonalizado(mensaje): #mensaje es una variable Local, uso solo dentro de funcion

#     return mensaje

# print(imprimeMensajePersonalizado("Este texto esta almacenado en mensaje"))

def imprimeOperacion(mensaje, num1, num2):

    return mensaje + str((num1+num2))

print(imprimeOperacion("La suma es: ", 5, 7))