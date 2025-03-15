#biblioteca para o "os" para o funcionamento do "cls" | linha 47: os.system("cls")
import os

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


print("-----------------calculadora-----------------")
num1 = int(input("digite um numero:"))
print("---------------------------------------------")

tentenovamente = 1

while tentenovamente:
    print("---------------------------------------------")
    print("digite .+. para uma operação de soma")
    print("digite .-. para uma operação de subitração")
    print("digite .x. para uma operação de multiplicação")
    print("digite .:. para uma operação de divisão")
    print("---------------------------------------------")
    selecionador = input(f"escolha o tipo de operação que dejesa:")
    print("---------------------------------------------")
    if (selecionador == '+'):
        tentenovamente = 0
    elif (selecionador == '-'):
        tentenovamente = 0
    elif (selecionador == ':'):
        tentenovamente = 0
    elif (selecionador == 'x'):
        tentenovamente = 0
    else:
        tentenovamente = 1
    os.system("cls")

num2 = int(input("digite o segundo numero numero:"))
print("---------------------------------------------")

if (selecionador == '+'):
        print(f"{num1} + {num2} = {num1 + num2}")
elif (selecionador == '-'):
        print(f"{num1} - {num2} = {num1 - num2}")
elif (selecionador == 'X'):
        print(f"{num1} X {num2} = {num1 * num2}")
elif (selecionador == ':'):
    if(num2 == 0):
        print("divisão com 0")
    else:
        print(f"{num1} : {num2} = {num1 / num2}")
