"""
Como criar e modificar arquivos com Python
'r' -> Abre para leitura - padrão
'w' -> Abre para escrita - sobrescreve caso o arquivo já exista
'a' -> Abre para escrita - adicionando o conteúdo ao final do arquivo
'r+' -> Abre para leitura e escrita
'wb' -> Abre para
'rb' -> Abre para

"""

import os

# with open('texto.txt', 'w', encoding='utf-8') as arquivo:
#     arquivo.write('Este é o meu arquivo\n')
    
# nomes = ['lucas', 'joão', 'maria', 'josé', 'pedro', 'ana', 'carlos', 'juliana', 'luciana', 'luciano']
# with open('texto.txt', 'a', encoding='utf-8', newline='') as arquivo:
#     for nome in nomes:
#         arquivo.write(nome + os.linesep)
   

# with open('texto.txt', 'r', encoding='utf-8') as arquivo:
#     print(arquivo.readlines())


# 🥇 DESAFIO Manipulação de Arquivos🥇
'''
Veja o desafio, tente fazer por conta própria e depois veja a solução que estou passando aqui
# Primeiro crie 3 listas
 * Uma lista que contem 5 frutas
 * Uma lista que contem 5 cores
 * Uma lista que contem 5 linguagens de programação
# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.
# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
'''

frutas = ['banana', 'maçã', 'uva', 'morango', 'abacaxi']
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']
linguagens = ['Python', 'Java', 'JavaScript', 'C#', 'C++']

# Desafio 1
with open('frutas.txt', 'w', encoding='utf-8', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

# Desafio 2   
with open('frutas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Desafio 3
with open('frutas.txt', 'a', encoding='utf-8', newline='') as arquivo:
    for cor in cores:
        arquivo.write(cor + os.linesep)

# Desafio 4
with open('Top 5 Linguagens.txt', 'w', encoding='utf-8', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)

# BONUS
# for i in range(10):
#     with open(f'arquivo_{i}.txt', 'w', encoding='utf-8', newline='') as arquivo:
#         pass
    
# 🥇 DESAFIO Manipulação de Arquivos 🥇

qtd_files = int(input('Quantos arquivos deseja criar? '))
file_name = input('Qual o nome dos arquivos? ')

file_type = ['.txt', '.csv', '.json', '.xml']

for file in file_type:
    for i in range(qtd_files):
        if not os.path.exists(f'C:\\Users\\gabri\\PythonAutodidata\\Colecoes\\{file_name}_{i}{file}'):
            with open(f'{file_name}_{i}{file}', 'w', encoding='utf-8', newline='') as arquivo:
                pass
        else:
            print(f'Arquivo do tipo {file_name}_{i}{file} já existe!')
    

