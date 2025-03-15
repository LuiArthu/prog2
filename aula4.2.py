def Fatorial (a):
    if a == 0:
        return 1
    else:
        return a * Fatorial (a - 1)
numero = 1
entrada = int(input("Numera para calcular o fatorial:"))
while numero <= entrada:
    print(Fatorial(numero))
    numero = numero + 1