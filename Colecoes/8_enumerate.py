# Enumerate - Enumerar elementos de uma coleção (lista, tupla, etc)
# Facilita a iteração sobre uma coleção e ao mesmo tempo obter o índice do elemento

for index, num in enumerate(range(1, 11), 1):
    print(f'Índice: {index} - Valor: {num}')
    if index == 5:
        print('Chegou ao índice 5')


nome = ['João', 'Maria', 'José', 'Pedro', 'Ana', 'Carlos', 'Marta', 'Paulo', 'Lucas', 'Mariana']

for index, nome in enumerate(nome, 1):
    print(f'Índice: {index} - Nome: {nome}')
    if index == 3:
        # Podemos trabalhar de acordo com o índice 
        print('Ja temos 3 nomes!')


frutas = ['Maçã', 'Banana', 'Uva', 'Morango', 'Pera']
for index, fruta in enumerate(frutas, 0):
    print(f'Índice: {index} - Fruta: {fruta}')
    if index == 3:
        print(f'N{index} - {fruta} Em promoção!')
    