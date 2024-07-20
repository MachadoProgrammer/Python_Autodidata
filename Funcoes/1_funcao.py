'''
def nome_da_funcao(parametros): -> caso necessário,  reduzir a quantidade de parâmetros por questaõ de boa prática
    # Código da função
    return valor_de_retorno

nome_da_funcao(argumentos) -> chamada da função
'''

def dar_boas_vindas(nome):
    print(f'Olá, {nome}! Seja bem-vindo(a) ao nosso jogo!')

dar_boas_vindas('Fulano')
    
# Valor padrão para o parâmetro
# caso tenha mais de um parâmetro com valor padrão, o parâmetro com valor padrão deve ser o último
def apresentar_lugar(horario_de_funcionamento, lugar='nossa loja',):
    print(f'Você está em {lugar}')



'''
# DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa
# DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade, 
# porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.
'''

def gerar_nome_completo(nome, sobrenome):
    print(f'Olá, {nome} {sobrenome}! Seja bem-vindo(a) ao nosso jogo!')

def calcular_valores(preco, quantidade=1):
    print(f'O valor total é de R${preco * quantidade}')

gerar_nome_completo('Fulano', 'de Tal')
calcular_valores(100, 3)