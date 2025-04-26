import sys
def fibo(numero):
	if numero == 1:
		return 1
	elif numero == 2:
		return 1
	else:
		return fibo(numero - 1) + fibo(numero - 2)

sys.set_int_max_str_digits(10000)
lista_fibo = []
seq = int(input("Digite o numero da sequencia desejada:"))
iterador = 1
while iterador <= seq:
	if iterador == 1 or iterador == 2:
		lista_fibo.append(1)
		print(f"Elemento: {iterador}: {lista_fibo[-1]}")
	else:
		lista_fibo.append(lista_fibo[-1] + lista_fibo[-2])
		print(f"Elemento: {iterador}: {lista_fibo[-1]}")
	#print(f"Elemento: {iterador}: {fibo(iterador)}")
	iterador += 1