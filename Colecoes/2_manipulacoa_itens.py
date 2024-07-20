# PODEMOS USAR O COMANDO dir(list), dir(str), etc para ver os métodos disponíveis para cada tipo de coleção

# Manipulando itens de uma lista

# Adicionando itens ao final da lista
lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)

# Unir listas
lista2 = [7, 8, 9]
lista.extend(lista2)
print(lista)

# Adicionar uma lista a outra e nao modificar a lista original
lista3 = [10, 11, 12]
lista4 = lista + lista3 

# Adicionar um item em uma posição específica
lista.insert(0, 0)
print(lista)

# Extrair com base no indice
print(lista.pop(0))

# Remover um item específico
lista.remove(1)
print(lista)

del lista[0:4]
print(lista)

# contando a ocorrencia de um item
print(lista.count(2))

# resetar a lista
lista.clear()
print(lista)

# ordenar a lista
lista = [4, 2, 1, 3]
lista.sort(reverse=True)
print(lista)

# reverse()