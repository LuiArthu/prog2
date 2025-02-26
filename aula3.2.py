print("-----------------calculadora-----------------")
num1 = int(input("digite um numero:"))
print("---------------------------------------------")


print("---------------------------------------------")
print("digite .+. para uma operação de soma")
print("digite .-. para uma operação de subitração")
print("digite .x. para uma operação de multiplicação")
print("digite .:. para uma operação de divisão")
print("---------------------------------------------")
selecionador = input(f"escolha o tipo de operação que dejesa:")
print("---------------------------------------------")
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
