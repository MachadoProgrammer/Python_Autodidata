# Argumentos posicionais -> diretamente relacionados a posição dos argumentos
# Todos os argumentos depois do * devem passar como argumento nomeados
def exibir_preco(produto,*, preco):
    print(f'O produto {produto} custa R${preco}')

# A ordem dos argumentos é importante
# TypeError: exibir_preco() takes 1 positional argument but 2 were given -> tipo de erro
exibir_preco('camisa', preco=50.00)

# Argumentos nomeados -> diretamente relacionados ao nome dos argumentos
# exibir_preco(preço=50.00, produto='camisa')



# Desafio 🥇
'''
Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato.
A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
Porém ela deve seguir as seguintes regras:
1 - O primeiro argumento deve ser posicional
2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeado

'''

def gerar_objeto_personalizado(cor,*, altura, formato):
    print(f'Cor: {cor}, Altura: {altura}, Formato: {formato}')

gerar_objeto_personalizado('azul', altura=10, formato='quadrado')