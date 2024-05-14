def gravar_nome_arquivo():
    nome = input("Maria Eduarda: ")
    with open("nome_usuario.txt", "w") as arquivo:
        arquivo.write(nome)
    print("Nome gravado com sucesso no arquivo nome_usuario.txt")

# Chamada da função para gravar o nome
gravar_nome_arquivo()





def copiar_conteudo_arquivo(nome_arquivo_origem, nome_arquivo_destino):
    try:
        with open(nome_arquivo_origem, "r") as arquivo_origem:
            conteudo = arquivo_origem.read()
        
        with open(nome_arquivo_destino, "w") as arquivo_destino:
            arquivo_destino.write(conteudo)
        
        print(f"Conteúdo do arquivo '{nome_arquivo_origem}' copiado para o arquivo '{nome_arquivo_destino}' com sucesso!")
    
    except FileNotFoundError:
        print("Arquivo de origem não encontrado.")
    except Exception as e:
        print("Ocorreu um erro:", e)

# Exemplo de uso
nome_arquivo_origem = "arquivo_origem.txt"
nome_arquivo_destino = "arquivo_destino.txt"
copiar_conteudo_arquivo(nome_arquivo_origem, nome_arquivo_destino)



def imprimir_conteudo_arquivo():
    nome_arquivo = input("Digite o nome do arquivo de texto: ")

    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo", nome_arquivo, ":\n", conteudo)

# Chamada da função para imprimir o conteúdo do arquivo
imprimir_conteudo_arquivo()



def encontrar_nome_por_numero(numero_procurado):
    try:
        with open("exemplo.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.split()
                numero = int(partes[0])
                nome = " ".join(partes[1:])
                if numero == numero_procurado:
                    return nome
        return None  # Se o número não for encontrado
    
    except FileNotFoundError:
        print("Arquivo de exemplo não encontrado.")
        return None
    except Exception as e:
        print("Ocorreu um erro:", e)
        return None

# Exemplo de uso
numero_procurado = int(input("Digite o número a ser procurado: "))
nome_encontrado = encontrar_nome_por_numero(numero_procurado)
if nome_encontrado:
    print("Nome correspondente ao número:", nome_encontrado)
else:
    print("Número não encontrado no arquivo.")
