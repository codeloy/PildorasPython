def divide():

    try:
        op1 = float(input("Introduce el 1º numero: "))
        op2 = float(input("Introduce el 2º numero: "))
        print(f"El resultado es: {op1/op2}")

    except ZeroDivisionError:
        print("No se puede dividir por 0")

    except ValueError:
        print("El valor introducido no es numerico")

    finally:
        print("Se ha intentado ejecutar el codigo en su totalidad")


divide()

print("calculo finalizado. Continuamos con el programa")
