import random

def lancar_dado():
    # Gerar um número aleatório entre 1 e 6 (representando as faces do dado)
    resultado = random.randint(1, 6)
    return resultado

# Chamada da função e exibição do resultado
print("O resultado do lançamento do dado é:", lancar_dado())




# random.randint(a, b) gera números inteiros entre a e b, ambos incluídos
num_inteiro = random.randint(1, 10)
print(f"Número inteiro aleatório entre 1 e 10: {num_inteiro}")
# random.uniform(a, b) gera números reais entre a e b, ambos incluídos
num_flutuante = random.uniform(1.5, 5.5)
print(f"Número de ponto flutuante aleatório entre 1.5 e 5.5: {num_flutuante}")


def sorteio_premios():
 premios = ["Carro", "Viagem", "Notebook", "Smartphone"]
 participante = input("Digite seu nome: ")
 premio = random.choice(premios)
 print(f"Parabéns, {participante}! Você ganhou um(a) {premio}.")