def bombom(dinheiro,preco):
    return float(dinheiro)/preco, dinheiro%preco


def maisbombom(dinheiro,preco):
    return preco - bombom(dinheiro,preco)[1]


def numeros_pares(numero):
    return list(range(2, numero + 1, 2))

# Exemplo de uso
numero = int(input("Digite um número inteiro: "))
pares = numeros_pares(numero)
print("Números pares até", numero, ":", pares)