class persona():
    __nombre = ""
    apellido = ""
    __edad = 0
    genero = "sin definir"

    def __init__(self, nombre, apellido, genero):
        self.apellido = apellido

        self.genero = genero
        self.__nombre = nombre

    def setEdad(self, laEdad): # Encapsulado con el metodo getter(setEdad)

        if laEdad < 0 or laEdad > 100:
            print("La edad no es correcta")
        else:
            self.__edad = laEdad
            return self.__edad

    def habla(self):
        return "La persona que se llama " + self.__nombre + "esta hablando"

    def camina(self):
        return "La persona que se llama " + self.__nombre + "esta caminando"

    def getDatos(self):  # getDatos nos devuelve lo almacenado en el constructor
        return "Nombre: " + self.__nombre + " apellido: " + self.apellido + \
            " edad: " + str(self.__edad) + " genero: " + self.genero


p1 = persona("Eloy", "Arana", "Masculino")

p1.setEdad(110)
print(p1.getDatos())
print(p1.getDatos())
p1.__nombre = "Alicia" #No cambia el nombre x q esta encampsulado con setter
