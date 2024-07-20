# Como podemos criar listas ?

# Loops e Range()
numeros = []
for i in range(10):
    numeros.append(i)

# Map() - Função que recebe uma função e uma coleção de dados
# e aplica a função a cada elemento da coleção
nomes = ['Ana', 'Maria', 'José', 'Pedro']


def aprovar(nome):
    # Logica mais complexa 
    # verificar a pontuação do aluno no banco de dados
    # verificar se o pagamento foi feito em uma planilha
    return f'{nome} foi aprovado'


print(list(map(aprovar, nomes)))

# DESAFIO -

# Extraia as cores da lista a seguir e coloque as em uma nova lista. Finalmente imprima a nova lista na tela.

pinturas = [

    ['Pintura Classica', 'Azul', 1857],

    ['Pintura Medieval', 'Vermelha', 1867],

    ['Pintura Moderna', 'Verde', 1897]

]

lista_cores = []
for pintura in pinturas:
    lista_cores.append(pintura[1])

print(lista_cores)

# def extrair_cor(pintura):
#     return pintura[1]

# lista_pintura = list(map(extrair_cor, pinturas))
