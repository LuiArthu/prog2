# --- Exemplo 1: Escrita com 'w' (Cria ou Sobrescreve) ---
# Este código cria 'diario.txt' ou apaga o conteúdo se ele já existir.
print("\n\n\nprimeiro exemplo")
print("Escrevendo/Sobrescrevendo 'diario.txt'...") # Imprime uma mensagem inicial para o usuário
try: # Inicia um bloco "tente fazer isso" para lidar com possíveis erros
    # Abre o arquivo 'diario.txt'.
    # 'w': Modo de ESCRITA. Se o arquivo não existe, ele CRIA. Se EXISTE, ele APAGA TODO O CONTEÚDO ANTIGO.
    # encoding='utf-8': Recomendado para suportar acentos e caracteres especiais.
    # 'as f': O arquivo aberto é associado à variável 'f'. Usaremos 'f' para interagir com o arquivo.
    with open('diario.txt', 'w', encoding='utf-8') as f:
        f.write("Primeira linha do diário.\n") # Escreve esta string no arquivo.
        # '\n': Caractere especial para PULAR LINHA. Sem ele, tudo ficaria na mesma linha.
        f.write("O modo 'w' começa o arquivo do zero.\n") # Escreve mais uma linha.
        f.write("Acentuação funciona!\n")   
        f.write("a")   
    # Quando o bloco 'with' termina (aqui), o arquivo 'f' é AUTOMATICAMENTE fechado.
    print("Arquivo 'diario.txt' escrito com sucesso.") # Mensagem de sucesso.
except Exception as e: # Se qualquer erro ocorrer dentro do bloco 'try' (ex: falta de permissão para criar o arquivo)...
    print(f"Ocorreu um erro ao escrever: {e}") # ...imprime uma mensagem com o erro.
#________________________________________________________________________________________________________________________

# # --- Exemplo 1.2: Escrita com 'w' (Cria ou Sobrescreve) ---
# Este código cria 'diario.txt' ou apaga o conteúdo se ele já existir.
print("\n\n\nprimeiro.2 exemplo")
print("Escrevendo/Sobrescrevendo 'diario_2.txt'...")
try: 
    with open('diario_2.txt', 'w', encoding='utf-8') as f:
        f.write("Primeira linha do diário.\n") 
        f.write("O modo 'w' começa o arquivo do zero.\n")
        f.write("Acentuação funciona!\n")   
        f.write("a")   
    print("Arquivo 'diario_2.txt' escrito com sucesso.") 
except Exception as e: 
    print(f"Ocorreu um erro ao escrever: {e}") 
#________________________________________________________________________________________________________________________

#--- Exemplo 2: Anexando com 'a' ---
# Este código adiciona conteúdo ao final de 'diario.txt' sem apagar.
print("\n\n\nsegundo exemplo")
print("\nAdicionando mais conteúdo ao 'diario_2.txt'...") # Mensagem para o usuário.
try:
    item_novo = "Esta linha foi adicionada depois.\n" # O texto que queremos adicionar.
    # Abre 'diario.txt' em modo ANEXAR ('a').
    # Se o arquivo não existir, ele CRIA. Se EXISTE, ele posiciona para escrever NO FINAL.
    with open('diario_2.txt', 'a', encoding='utf-8') as f:
        f.write(item_novo) # Escreve o novo item.
    print("Linha anexada com sucesso.")

    item_novo_2 = "Mais uma linha anexada.\n" # Mais um texto.
    with open('diario_2.txt', 'a', encoding='utf-8') as f: # Abre de novo em modo 'a'.
        f.write(item_novo_2) # Adiciona.
    print("Outra linha anexada com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro ao anexar: {e}")

#________________________________________________________________________________________________________________________

# --- Exemplo 3: Lendo o conteúdo inteiro com read() ---
# Bom para arquivos pequenos.
print("\n\n\nterceiro exemplo")
print("\nLendo o conteúdo completo de 'diario.txt' de uma vez...")
try:
    # Abre 'diario.txt' em modo LEITURA ('r').
    # Se o arquivo não existir, um erro FileNotFoundError ocorrerá.
    with open('diario.txt', 'r', encoding='utf-8') as f:
        conteudo_total = f.read() # O método .read() lê TODO o arquivo para uma ÚNICA string.
        print("--- Conteúdo Completo ---")
        if conteudo_total: # Verifica se a string 'conteudo_total' não está vazia.
            print(conteudo_total) # Imprime o conteúdo.
        else:
            print("(Arquivo vazio)") # Se estava vazio.
        print("--- Fim do Conteúdo ---")
except FileNotFoundError: # Captura especificamente o erro se o arquivo não for encontrado.
    print("Erro: O arquivo 'diario.txt' não foi encontrado.")
except Exception as e: # Captura outros possíveis erros de leitura.
    print(f"Ocorreu um erro ao ler: {e}")

#________________________________________________________________________________________________________________________

# --- Exemplo 4: Lendo linha por linha (Método preferido) ---
print("\n\n\nquarto exemplo")
print("\nLendo 'diario_2.txt' linha a linha...")
try:
    with open('diario_2.txt', 'r', encoding='utf-8') as f: # Abre para leitura
        print("--- Linhas do Arquivo ---")
        tem_conteudo = False # Uma "flag" para saber se o arquivo tinha algo
        # Iterar diretamente sobre o objeto arquivo 'f' lê uma linha por vez.
        # 'enumerate(f)' nos dá o índice 'i' (começando em 0) e a 'linha'.
        for i, linha in enumerate(f):
            tem_conteudo = True # Marca que processamos pelo menos uma linha
            # Cada 'linha' lida do arquivo termina com um caractere de nova linha ('\n').
            # '.strip()' remove espaços em branco e o '\n' do início e do fim da string.
            print(f"Linha {i+1}: {linha.strip()}")
        if not tem_conteudo: # Se o loop não executou nenhuma vez (arquivo vazio)
            print("(Arquivo vazio)")
        print("-----------------------")
except FileNotFoundError:
    print("Erro: O arquivo 'diario_2.txt' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler linha por linha: {e}")

#________________________________________________________________________________________________________________________

print("\n\n\ncriando arquivo exemplo")
print("Escrevendo/Sobrescrevendo 'numeros.txt'...")
try: 
    with open('numeros.txt', 'w', encoding='utf-8') as f:
        f.write("\n")
    print("numeros.txt' escrito com sucesso.")

except Exception as e: 
    print(f"Ocorreu um erro ao escrever: {e}") 

# --- Exemplo 5: Lendo números e somando ---
# 1.  Crie manualmente um arquivo chamado 'numeros.txt' na mesma pasta.
# 2.  Coloque números dentro dele, um por linha (ex: 10, 5.5, -3, 20).
print("\n\n\nultimo exemplo")
print("\nLendo e somando números de 'numeros.txt'...")
soma = 0.0 # Inicializa a soma como float para aceitar decimais
numeros_lidos = [] # Lista para guardar os números que conseguimos ler e converter
try:
    with open('numeros.txt', 'r', encoding='utf-8') as f: # Abre para leitura
        for linha in f: # Lê linha por linha
            linha_limpa = linha.strip() # Limpa a linha
            if linha_limpa: # Só processa se a linha não estiver totalmente em branco
                try:
                    # PONTO CRUCIAL: Converter a string lida para número!
                    # Usamos float() para aceitar tanto inteiros quanto decimais.
                    numero = float(linha_limpa)
                    numeros_lidos.append(numero) # Guarda o número na lista
                    soma += numero # Acumula na variável 'soma'
                    print(f"Lido: {numero}")
                except ValueError: # Se a linha não puder ser convertida para float...
                    # (Ex: se tiver texto como "abc" no meio dos números)
                    print(f"Aviso: Ignorando linha inválida -> '{linha_limpa}'")

    if numeros_lidos: # Se a lista 'numeros_lidos' não estiver vazia
        print(f"Números lidos: {numeros_lidos}")
        print(f"Soma total: {soma}")
    else: # Se nenhum número válido foi encontrado no arquivo
        print("Nenhum número válido encontrado no arquivo.")

except FileNotFoundError: # Se o arquivo 'numeros.txt' não for encontrado
    print("Erro: Arquivo 'numeros.txt' não encontrado. Crie-o primeiro.")
except Exception as e: # Para outros erros inesperados
    print(f"Ocorreu um erro inesperado: {e}")