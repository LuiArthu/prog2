print("bem vindo!")

class perfil():
    def registrar_funcio():
        novo_funcionario = input ("Nome:")
        cpf = input("cpf:")
        idade = input("idade:")
        mae = input("mae:")

        try:
            with open('lista_de_funcionarios.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{novo_funcionario}\n")        
            print("funcionario adicionado com sucesso!") 
        except Exception as e: 
            print(f"Ocorreu um erro ao adicionar um novo funcionario: {e}") 
        try:
            with open('perfil_funcio.txt', 'a', encoding='utf-8') as f:
                f.write(f"{cpf}\n")
                f.write(f"{idade}\n")
                f.write(f"{mae}\n")    
                f.write(f"\n")    
            print("funcionario adicionado com sucesso!") 
        except Exception as e: 
            print(f"Ocorreu um erro ao adicionar um novo funcionario: {e}") 



class funcionarios(perfil):
    def ver_funcionarios():
        try:
            with open('lista_de_funcionarios.txt', 'r', encoding='utf-8') as f:
                print("--- funcionarios registrados ---")
                tem_funcionario = False 
                for i, linha in enumerate(f):
                    tem_funcionario = True 
                    print(f"item {i+1}: {linha.strip()}")
                if not tem_funcionario: 
                    print("(sem funcionarios)")
                print("-----------------------")
        except FileNotFoundError:
            print("Erro: O arquivo 'lista_de_funcionarios.txt' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao ler linha por linha: {e}")

    def refazer():
        try:
            funcionarios_troca = int(input("qual item deseja mudar:"))
            with open('lista_de_funcionarios.txt', 'r+', encoding='utf-8') as f:
                print("--- itens no Arquivo ---")
                tem_conteudo = False
                for i, linha in enumerate(f):
                    tem_conteudo = True
                    i = 1 + i
                    if(i == funcionarios_troca):
                        novo_funcionarios = input(f"novo nome do item {i}:")
                        f.seek(i)
                        f.write(f"\n{novo_funcionarios}\n")    
                    if(i != funcionarios_troca):
                        print(f"item {i}: {linha.strip()}")
                    if not tem_conteudo: 
                        print("(Arquivo vazio)")
                    print("-----------------------")
        except FileNotFoundError:
            print("Erro: O arquivo 'lista_de_funcionarios.txt' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao ler linha por linha: {e}")



                








    sair = 1
    while (sair):
        print("digite 1 para adicinar um novo funcionario")
        print("digite 2 para ver lista de funcionsrios")
        print("digite 3 trocar funcionario")
        print("digite 4 para finalizar a seção")
        escolha = int(input("escolha:"))
        if (1 == escolha):
            perfil.registrar_funcio()
        elif(2 == escolha):    
            perfil.registrar_funcio()
        elif(3 == escolha):
            refazer()
        elif(4 == escolha):    
            sair = 0
            print("obrigado por sua presença ou visita")
        else:
            print("valor não aceito")
