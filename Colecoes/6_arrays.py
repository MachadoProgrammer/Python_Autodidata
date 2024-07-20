# Array -> Armazena uma coleção de items, mas do mesmo tipo

from array import array

# Criando um array de inteiros
numeros = array('i', [1, 2, 3, 4, 5])
print(numeros)
numeros.append(6)
print(numeros)
numeros.insert(3, 40)
print(numeros)
numeros.pop(1)
print(numeros)
numeros.remove(3)
print(numeros)
del numeros[0]
print(numeros)