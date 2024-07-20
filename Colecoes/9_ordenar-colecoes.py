# Ordenar coleções através de propriedades
from operator import itemgetter

pessoas = [
    {'nome': 'João', 'idade': 20, 'nivel_acesso': '1'},
    {'nome': 'Maria', 'idade': 25, 'nivel_acesso': '2'},
    {'nome': 'José', 'idade': 30, 'nivel_acesso': '3'},
    {'nome': 'Pedro', 'idade': 35, 'nivel_acesso': '4'}
]

# Ordenar por nome
pessoas.sort(key=itemgetter('nivel_acesso'))
# print(pessoas)

produtos: list[tuple[str, int]] = [
  ('P1', 10),
  ('P2', 20),
  ('P3', 5),
  ('P4', 15)
]

produtos.sort(key=itemgetter(0)) # reverse=True
# print(produtos)


matriz = [[4, 5], [7, 8], [1, 2]]
matriz.sort(key=itemgetter(1))
# print(matriz)

# Ordene a lista de produtos abaixo pelo preço em ordem crescente
produtos1 = [
    {'nome': 'Celular',
     'preco': 1500
     },
    {'nome': 'Monitor',
     'preco': 500
     },
    {'nome': 'Microfone',
     'preco': 300
     }
]

produtos1.sort(key=itemgetter('preco'))
print(produtos1)


# Ordene em ordem descrescente a lista de equipamento_filmagem por valor do equipamento
equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200),
]

equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

# Ordene em ordem crescente a cotacao_moedas com base no valor da moeda
cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]

cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)