def imprimir_informacoes(nome, idade, cidade):
    print("Nome:", nome, sep=" ", end=" - ")
    print("Idade:", idade, sep=" ", end=" anos - ")
    print("Cidade:", cidade, sep=" ")

# Exemplo de uso da função
nome = "Maria"
idade = 21
cidade = "Vitoria da Conquista"

imprimir_informacoes(nome, idade, cidade)



def calcular_operacao():
    # Pedir ao usuário dois números e a operação desejada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Verificar a operação e calcular o resultado
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        # Verificar se o divisor não é zero
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero.")
            return
    else:
        print("Operação inválida.")
        return

    # Imprimir o resultado da operação
    print("O resultado de {} {} {} é: {}".format(num1, operacao, num2, resultado))

# Chamada da função
calcular_operacao()



def criar_lista_compras():
    # Solicitar ao usuário que digite os itens da lista de compras separados por vírgula
    entrada = input("Digite os itens da lista de compras separados por vírgula: ")

    # Dividir a entrada do usuário em uma lista de itens
    itens = entrada.split(',')

    # Imprimir os itens em linhas separadas usando um laço
    print("Lista de compras:")
    for item in itens:
        print(item.strip())  # strip() remove espaços em branco extras antes e depois do item

# Chamada da função
criar_lista_compras()


def celsius_para_fahrenheit():
    # Solicitar ao usuário a temperatura em graus Celsius
    celsius = float(input("23°: "))

    # Converter Celsius para Fahrenheit usando a fórmula (Celsius * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32

    # Imprimir o resultado
    print("A temperatura em Fahrenheit é:", fahrenheit, "°F")

# Chamada da função
celsius_para_fahrenheit()



def pedir_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        nomes.append(nome)

    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Chamada da função
pedir_nomes()
