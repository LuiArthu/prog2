def fibonacci (valor):
    if valor == 1:
        return 1
    elif valor == 2:
        return 1
    else:
        return fibonacci(valor - 1) + fibonacci (valor - 2)

escolha = int(input("digite um numero para ser calculado em fibonacci:"))
contador = 1
while escolha >= contador:
    print (fibonacci(contador))
    contador = contador + 1


print("hello world")