# NESTED LOOPS - Loop dentro de outro loop (loop aninhado)

paises = ['Brasil', 'Argentina', 'Uruguai', 'Chile']
cidades = ['São Paulo', 'Buenos Aires', 'Montevidéu', 'Santiago']

for pais in paises:
    for cidade in cidades:
        print(f'{cidade} é uma cidade de {pais}')

# interando / iteravel
for x in range(1, 11):
    for y in range(1, 6):
        print(f'Valor externo x: {x} e valor interno y: {y}')


# Iteravel -> iterando sobre um iteravel 