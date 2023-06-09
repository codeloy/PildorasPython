class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getDatosPersonales(self):
        return " Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)

    def habla(self):
        return "Estoy hablando"

    def piensa(self):
        return "Estoy pensando"

    def camina(self):
        return "Estoy caminando"

    def come(self):
        return "Estoy caminando"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, escuela):
        super().__init__(nombre, apellido, edad)
        self.escuela = escuela

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Escuela: " + self.escuela

    def estudia(self):
        return "Estoy estudiando"


persona1 = Persona("Ana", "Gomez", 31)
estudiante1 = Estudiante("Eloy", "Arana", 42, "Tecnica nº1")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
