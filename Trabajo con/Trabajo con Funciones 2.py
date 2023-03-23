

def ImprimeMensajes():  # Definicion o creacion de la Función

    return "Este es el mensaje de la Función"


def ImprimeMensajePersonalizado(mensaje, valor1, valor2):

    return mensaje + str((valor1+valor2))# uso str() porque no puedo concatenar numero y texto

print(ImprimeMensajePersonalizado("La suma es ",5,7))# son los valores de mensaje, valor1, valor2 