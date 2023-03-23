

def evaluarAlumno(nota):
    valoracion = "Desconocida"

    if nota < 5:
        valoracion = "suspenso"

    elif (nota > 10):
        valoracion = "Nota incorrecta"

    else:
        valoracion = "Aprobado"
    return valoracion


notaAlumno = int(input("introduce la nota: "))#uso int() porque la consola pasa todo a texto
print(evaluarAlumno(notaAlumno))
