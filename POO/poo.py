

class coche():
    ruedas = 4  # Propiedades
    largoChasis = 260
    anchoChasis = 130
    arrancando = False

    def arrancar(self):  # Comportamiento. Self almacena renault/mazda para arrancarlo
        self.arrancando = True  # Arranca mazda o renalt

    def estadoCoche(self):
        if (self.arrancando):
            return "El coche esta funcionando"

        else:
            return "El coche esta parado"


mazda = coche()  # Ejemplar de clase

renault = coche()

print("Tu coche tiene " + str(renault.ruedas) + " ruedas")

renault.arrancar()

print(f"Tu coche esta arrancado: {renault.arrancando}")

print(renault.estadoCoche())
