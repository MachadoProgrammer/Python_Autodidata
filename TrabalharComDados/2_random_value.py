# Valores aleatorios com random

# Pode ter uso para:
# - Criar senhas seguras
# - Escolher um item aleatório de uma lista(baralho, lista de musicas, etc)
# - Gerar nomes aleatórios

import random

# Gerando um valor aleatório
value = random.random()

# Gerando um valor decimal de valor minimo ao maximo 
value = random.uniform(1, 10)

# Gerando um valor inteiro de valor minimo ao maximo
value = random.randint(1, 6)

# Escolhendo um valor aleatório de uma lista
greetings: list[str] = ['Hello', 'Hi', 'Hey', 'Howdy']
random.choices(greetings, k=2) # k=2 - escolhe 2 valores aleatórios

# Embaralhando uma lista
deck = list(range(1, 53))
random.shuffle(deck) 

# Desafios Random 
'''
1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
    jogue as opções dentro de uma variável e depois crie um programa que imprimir 'cara' ou 'coroa' na tela

2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
    Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela

3. você quer escolher aleatóriamente um número de 10-100
    Imprima na tela um valor aleatório entre 10 e 100'''

# Desafio 1
coin = ['Cara', 'Coroa']
print(random.choice(coin))

# Desafio 2
names = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos']
print(random.choice(names))

# Desafio 3
print(random.randint(10, 100))
