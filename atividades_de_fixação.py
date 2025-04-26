#1) Par ou ímpar. Escreva uma função que receba um número e retorne se ele é par ou ímpar.

def parouimpar (n):
    if ( n % 2 == 0):
        print("Par")
    else:
        print("Impar")

parouimpar(4)
parouimpar(3)

#2) Maior de dois números. Crie uma função que receba dois números e retorne o maior deles.

def maior_n (n1, n2):
    if (n1 < n2):
        print ("O numero", n2 ,"e maior que o numero", n1 , ".")
    elif (n1 > n2):
        print ("O numero", n1 ,"e maior que o numero", n2 , ".")
    elif (n1 == n2):
        print ("O numero", n1 ,"e", n2 , "são iguais.")
    
maior_n (3, 5)
maior_n (6, 5)
maior_n (0, 0)

#3) Contagem regressiva. Faça uma função que receba um número inteiro positivo e use um while para imprimir uma contagem regressiva até 0.
def contagem(n):
    fim = 1
    while (fim):
        
        print (n)
        if n < -0:
            n = n + 1
        elif n < fim:
            fim = 0
        else:
            n = n - 1

contagem(3)
contagem(-3)

#4) Fatorial (com for). Escreva uma função que calcule o fatorial de um número usando um loop for.

def Fatorial (a):
    if a == 1:
        return 1
    else:
        return a * Fatorial (a - 1)
numero = 1
entrada = int(input("Numera para calcular o fatorial:"))
for numero in range(entrada):
    print(Fatorial(numero + 1))

#5) Fatorial recursivo. Escreva uma função recursiva que calcule o fatorial de um número.

def Fatorial (a):
    if a == 1:
        return 1
    else:
        return a * Fatorial (a - 1)

entrada = int(input("Numera para calcular o fatorial:"))

print(Fatorial(entrada))

#6) Soma de números pares até N. Faça uma função que receba um número n e some todos os números pares de 0 até n.

def soma_de_n_pares(n):
    fim = 1
    if (n % 2 == 0):
        resultado = n 
        fim = 1
        while fim:
            if (n <= 0):
                print(resultado)
                fim = 0
            elif (n > 0):
                n = n - 2
                resultado = n + resultado
    else:
        n = n - 1

soma_pares = int(input("soma de pares:"))

soma_de_n_pares(soma_pares)

#7) Verifica número primo. Crie uma função que verifique se um número é primo usando um loop for.

def numero_primo(num):
    if (num <= 1):
        print("O numero", num ,"não é primo")
    elif (num == 2):
        print("O numero", num ,"é primo")
    elif (num % 2 == 0):
        print("O numero", num ,"não é primo")
    elif (num == 3):
        print("O numero", num ,"é primo")
    else:
        resultado = num / 2
        resultado = int(resultado)

        for tempo in range (3, resultado, 2):
            if (num % tempo == 0):
                print(f"O numero {num} mod {tempo} é: {num % tempo}")
                return print("O numero", num ,"não é primo")
        return print("O numero", num ,"é primo")

primo = int(input("primo?"))   
numero_primo(primo)        


#8) Inverter string. Faça uma função que receba uma string e retorne a string invertida (primeiramente sem usar .reverse() ou [::-1], depois podem testar caso queiram).


#9) Contador de vogais. Escreva uma função que conte quantas vogais existem em uma string (desconsidere acentos).
#10) Sequência de Fibonacci (recursiva).Crie uma função recursiva que retorne o n-ésimo número da sequência de Fibonacci.
#11) Soma de dígitos recursivos. Crie uma função recursiva que calcule a soma de todos antecessores de um número inteiro.

#BONUS
#12) Soma de dígitos recursivamente + Crie uma função recursiva que calcule a soma de todos os dígitos de um número inteiro.