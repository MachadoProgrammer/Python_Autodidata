# JSON -> JavaScript Object Notation
# É um formato de dados muito utilizado para interoperabilidade de sistemas

import json

with open('arquivosJson/usuarios1.json', 'r', encoding='utf-8') as f:
    dados = json.load(f) # converte o arquivo json -> string -> dicionário
    # print(dados['nome'])

# Lendo um arquivo json com múltiplos registros
with open('arquivosJson/usuarios2.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
    # for permissao in dados['permissões']:
    #     print(permissao)

# Lendo um arquivo json com múltiplos registros
with open('arquivosJson/usuarios3.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
    # print(dados['usuários'][1]['admin'])
    

# Lendo um arquivo json com múltiplos registros
with open('arquivosJson/usuarios4.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
    # print(dados['usuários'][0]['plano']['preco'])


# Lendo um arquivo json com múltiplos registros
with open('arquivosJson/usuarios5.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
    # print(dados[0]['admin'])


# Imprimir o e-mail do usuário com id 2
# imprimir a city do usuário com id 1
# Imprimir o total do pedido do usuário com id 2

with open('arquivosJson/desafio.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
    print(dados['user'][1]['id'])
    print(dados['user'][0]['address']['city'])
    print(dados['user'][1]['orders'][0]['total'])
