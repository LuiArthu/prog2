#vetores são caixas e podemos armazenar dados

A = [0, 1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
B = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
C = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
print(f"Elementos de A: {A [3]}") #lista
print(f"Elementos de B: {B [3]}") #de vetores 
print(f"Elementos de C: {C [2] [1]}") # 2 É Linha e 1 É coluna

elemento = C [1] [0]
print(elemento)

def Valores_C (valor1,valor2):
    print(C[valor1][valor2])
    

num1 = 0
num2 = 0
while num2 <= 3 and num1 <= 2:
    Valores_C (num1,num2)
    if num2 >= 2:
        num2 = num2 + 1
    else:
        num2 = 0
        num1 = num1 + 1
    
