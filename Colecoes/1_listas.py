# Listas são coleções de itens em uma ordem específica. Aceitam itens duplicados e são mutáveis e qualquer tipo de dado.
# São representadas por colchetes [].

# Criando uma lista
lista = [1, 2, 3, 4, 5]
print(lista[lista.index(2)]) # Acessando um item da lista

# Multiplicando uma lista
lista = [9] * 5
print(lista)

# Criando uma lista usando gerador Range
lista1 = list(range(1, 11))
print(lista1)

# Gerar a partir de uma string
lista2 = list('Python')
print(lista2)

# Lista de listas(matriz)
matriz = [['Carol',30], ['João', 25], ['Maria', 20]]
print(matriz[2][0])


# Desafios 🥇

''' 
Desafio #1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ele na tela
Desafio #2 Usando apenas uma linha de código, crie uma lista de 10 a 131
Desafio #3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2
Desafio #4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos
 que você mais usa durante o dia, mas agora dentro de cada item você vai colocar 
uma informação extra, coloque o valor em reais desse objeto também e imprima ele 
na tela  
'''

