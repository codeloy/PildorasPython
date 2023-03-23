
class CuentaCorriente():

    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo

    def getDatos(self):
        return "El titular de la cuenta nº " + self.numeroCuenta + " es " + self.titular + \
            " y tiene un saldo de cuenta de: " + str(self.saldo) + " euros"

    def ingreso(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retiro(self, cantidad):
        self.saldo = self.saldo - cantidad


c1 = CuentaCorriente("3289329900", "Eloy", 35000)

c1.ingreso(5000)

c1.retiro(1500)

print(c1.getDatos())
