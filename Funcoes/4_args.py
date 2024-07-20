# Funções com n° de argumentos dinâmicos 
def somar(*valores, b):
    print(valores + b)
    for v in valores:
        b += v
    print(b)
# *valores -> recebe uma tupla com todos os valores passados

somar(1, 2, 3, 4, 5, b=6) # O b precisa ser passado como argumento nomeado   


