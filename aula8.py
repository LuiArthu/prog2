print("bem vindo!")
def adcinor_item():
    novo_item = input ("qual item você dejesa adicinor ao itens de compra:")
    try: 
        with open('lista_de_compras.txt', 'a', encoding='utf-8') as f:
                f.write(f"{novo_item}\n")        
        print("Arquivo 'lista_de_compras.txt' escrito com sucesso.") 
    except Exception as e: 
        print(f"Ocorreu um erro ao escrever: {e}") 
  

def ver():
    try:
        with open('lista_de_compras.txt', 'r', encoding='utf-8') as f:
            print("--- itens no Arquivo ---")
            tem_conteudo = False 
            for i, linha in enumerate(f):
                tem_conteudo = True 
                print(f"item {i+1}: {linha.strip()}")
            if not tem_conteudo: 
                print("(Arquivo vazio)")
            print("-----------------------")
    except FileNotFoundError:
        print("Erro: O arquivo 'lista_de_compras.txt' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler linha por linha: {e}")

def refazer():
    try:
        item_troca = int(input("qual item deseja mudar:"))
        with open('lista_de_compras.txt', 'r', encoding='utf-8') as f:
            print("--- itens no Arquivo ---")
            tem_conteudo = False
            for i, linha in enumerate(f):
                tem_conteudo = True
                i = 1 + i
                if(i == item_troca):
                    novo_item = input(f"novo nome do item {i}:")
                    with open('lista_de_compras.txt', 'r+', encoding='utf-8') as f:
                        f.seek(i)
                        f.write(f"\n{novo_item}\n")    
                if(i != item_troca):
                    with open('lista_de_compras.txt', 'r', encoding='utf-8') as f:  
                        print(f"item {i}: {linha.strip()}")
                if not tem_conteudo: 
                    print("(Arquivo vazio)")
                print("-----------------------")
    except FileNotFoundError:
        print("Erro: O arquivo 'lista_de_compras.txt' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler linha por linha: {e}")

sair = 1
while (sair):
    print("digite 1 para adicinar um novo item")
    print("digite 2 para ver lista")
    print("digite 4 para finalizar a seção")
    escolha = int(input("escolha:"))
    if (1 == escolha):
        adcinor_item()
    elif(2 == escolha):    
        ver()
    elif(3 == escolha):
        refazer()
    elif(4 == escolha):    
        sair = 0
        print("obrigado por sua presença ou visita")
    else:
        print("valor não aceito")
