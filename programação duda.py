def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

# Exemplo de uso:
numeros = [1, 2, 3, 4]
soma, media = calcular_soma_e_media(numeros)
print("Soma:", soma)
print("Média:", media)


def substituir_palavra(lista, palavra_procurada, nova_palavra):
    for i in range(len(lista)):
        if lista[i] == palavra_procurada:
            lista[i] = nova_palavra
    return lista

# Exemplo de utilização da função
lista_palavras = ["uva", "morango", "limão"]
palavra_procurada = "uva"
nova_palavra = "maçã"

lista_alterada = substituir_palavra(lista_palavras, palavra_procurada, nova_palavra)
print("Lista alterada:", lista_alterada)


def imprimir_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Exemplo de utilização da função
n = 7
imprimir_triangulo(n)