# Trabalhando com multiplas listas
from itertools import zip_longest



a_list = ['A', 'B', 'C', 'D']
b_list = [1, 2, 3, 4]

for a, b in zip(a_list, b_list):
    print(a, b)

produtos = ['arroz', 'feijao', 'macarrao']
precos = [2.99, 3.99, 1.99]

for produto, preco in zip(produtos, precos):
    print(f'{produto} - R$ {preco:.2f}')


# Usando zip para criar um dicionario
dicionario = dict(zip(a_list, b_list))
print(dicionario)



titulos = ['titulo1', 'titulo2', 'titulo3', 'titulo4']
valores = [1, 2]

for titulos, valores in zip_longest(titulos, valores):
    print(f'Encontramos o {titulos} com o valor {valores}')


# DESAFIOS 🥇

## DESAFIO 1

# Usando as listas abaixo:

# produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']

# precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

# Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas, porém a pesquisa foi encontrada em momentos diferentes, assim acabamos com duas listas diferentes, favor criar uma mensagem que diz o nome e valor produto, como as mensagens abaixo:

# Produto: Produto 1 encontrado no valor de R$500,00

# Produto: Produto 2 encontrado no valor de R$1500,00

# Produto: Produto 3 encontrado no valor de R$2700,00

# Produto: Produto 4 encontrado no valor de R$5000,00

# Produto: Produto 5 encontrado no valor de None  

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

for produto, preco in zip_longest(produtos, precos):
    print(f'Produto: {produto} encontrado no valor de {preco}')