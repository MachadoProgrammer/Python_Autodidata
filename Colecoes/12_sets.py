# SET -> recebe valores, não aceita repetição e não tem índice
# SET -> não é ordenado
# SET -> não é indexado


numeros = {1, 2, 2, 3, 5}

nummeros_set = set(numeros)
# print(nummeros_set)

# add() -> adiciona um elemento ao set

nummeros_set.add(6)
# print(nummeros_set)

# conjuntos
numeros1 = {1, 2, 3, 4, 5}
numeros2 = {4, 5, 6, 7, 8}

a = numeros1
b = numeros2

print(a.symmetric_difference(b))
print(a.intersection(b))
print(a.union(b))