

num1 = int(input("introduce el primer numero "))

num2 = int(input("introduce el segundo numero "))


def es_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    print(str(numero) + " es primo")
    return True


for i in range(num1, num2):
    es_primo(i)
