C = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]

def Valores_C (valor1,valor2):
    print(C[valor1][valor2])

num1 = 0
num2 = 0
limitador = 2
while num1 <= 2:
    Valores_C (num1,num2)

    if num2 < 2:
        num2 = num2 + 1
    elif num2 >= 2:
        num2 = 0
        num1 = num1 + 1