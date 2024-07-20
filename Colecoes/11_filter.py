nomes = ['Ana', 'Maria', 'José', 'Pedro']

def aprovar(nome):
    if nome == 'José':
        return True
    else:
        return False
    

print(list(filter(aprovar, nomes)))
print(list(map(aprovar, nomes)))


pinturas = [
    ['Monalisa', 1500000, 1956],
    ['Guernica', 1000000, 1937],
    ['Gioconda', 2000000, 1950],
    ['A Noite Estrelada', 2500000, 1889]
]

def antigas(pintura):
    if pintura[2] < 1950:
        return True
    else:
        return False
    
print(list(filter(antigas, pinturas)))

# DESAFIO 1 🥇

'''

Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500

'''

vagas = [

    ['vaga 1', 1200],

    ['vaga 2', 2550],

    ['vaga 3', 5000]

]     

def salario(vaga):
    if vaga[1] > 2500:
        return True
    else:
        return False
    
print(list(filter(salario, vagas)))