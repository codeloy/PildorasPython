print("Calculo de tipo impositivo para la renta de 2023")

renta = float(input("introduzca su el valor de su renta, por favor"))

if renta <= 12000:
    porcentaje = "7% de tipo impositivo"

elif renta > 12000 and renta < 18000:
    porcentaje = "15% de tipo impositivo"

elif renta > 18000 and renta < 35000:
    porcentaje = "21% de tipo impositivo"

elif renta > 35000 and renta < 70000:
    porcentaje = "35% de tipo impositivo"

elif renta > 70000:

    porcentaje = "45% de tipo impositivo"

print("A la renta " + str(renta) + " le corresponde un " + porcentaje)
