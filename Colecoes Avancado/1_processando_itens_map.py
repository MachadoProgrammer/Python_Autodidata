# Como podemos criar listas ? 
# Usando loops e Range()
numeros = []

for i in range(10):
    numeros.append(i)

# print(numeros)

# Usando o Map

nomes = ['João', 'Maria', 'José', 'Pedro', 'Ana', 'Carlos', 'Marta', 'Paulo', 'Lucas', 'Mariana']

def aprovar_pessoa(nome):
    return f'{nome} Aprovado'

aprovados = list(map(aprovar_pessoa, nomes))
# converter o resultado para uma lista
