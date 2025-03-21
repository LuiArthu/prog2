def Fibonacci (num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return Fibonacci (num - 1) + Fibonacci (num - 2)
numero = 1
entrada = int(input("Numera para calcular o fibonacci:"))
while numero <= entrada:
    print(f"fibonacci de {numero}:{Fibonacci(numero)}")
    numero = numero + 1


    