

def tabla_de_multiplicar(numero):
    print(f"La tabla de multiplicar del numero: {numero}")
    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} X {contador} = {operacion}")


tabla_de_multiplicar(3)
tabla_de_multiplicar(7)

print("---------------------_______________---------------------")

for numero_tabla in range(1, 11):
    tabla_de_multiplicar(numero_tabla)

print("\n##### Ejemplo2 #######")


def getEmpleado(nombre, dni=None):  # dni = None me permite no utilizar este parametro
    print("Empleado")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")


getEmpleado("Eloy", 3837282)

print("\n##### Ejemplo 3 #######")


def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo


print(saludame("Eloy"))

print("\n##### Ejemplo 4 #######")


def calculadora(num1, num2, basicas=False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2

    cadena = ""
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena


print(calculadora(8, 2, False))
print("\n##### Ejemplo 5 #######")


def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto


print(devuelveTodo("Eloy", "Arana"))

print("\n##### Ejemplo Funcion Lambda #######")

dime_el_year = lambda year: f"El año es: {year}"

print(dime_el_year(2023))