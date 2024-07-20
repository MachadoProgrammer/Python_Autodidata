# Dicionários são coleções de dados que possuem uma chave e um valor associado a ela.

pessoa = {'Matheus': 22, 'João': 25, 'Maria': 30}

print(pessoa.keys())  # Retorna as chaves do dicionário
print(pessoa.values())  # Retorna os valores do dicionário
print(pessoa.items())  # Retorna os itens do dicionário

# Iterando sobre um dicionário
for item in pessoa.items():
    print(item[0])

# Desempacotando um dicionário
for nome, idade in pessoa.items():
    print(nome, idade)

courses = []
with open("languagens.csv", encoding="utf-8") as file:
    for line in file:
        name, category = line.rstrip().split(",")
        course = {"name": name, "category": category}
        courses.append(course)
print(courses)

for course in courses:
    print(f"{course['name']} -{course['category']}")
