def somarateparar(a, b):
    iterador = 1
    soma = a + b
    while iterador:
        print(f"A soma atualmente é: {soma}")
        numero = int(input("O proximo número para a soma. Para parar, 0:"))
        soma = soma + numero

        if numero == 0:
            iterador = 0 
    print(f"No final, a soma é: {soma}")

var1 = int(input("digite um numero:"))
var2 = int(input("digite um numero:"))

somarateparar(var1, var2)