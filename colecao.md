# Coleções

-- Podemos usar o comando dir(list), dir(str), etc... para ver os métodos disponíveis para cada tipo de coleção

-- Processar multiplas listas -> zip, zip_longest -> from itertools
* zip_longest -> para caso uma lista seja maior que a outra

## Dicionários 

- Podem ser acessados por []

-- dict.keys() -> Retorna as chaves do dicionário
-- dict.values() -> Retorna as valores do dicionário
-- dict.items() -> Retorna chave e valor do dicionário

## Tuplas

-- Não é possível adicionar, remover ou alterar elementos de uma tupla.(index)
    1. Dentro de um programa onde os valores não podem ser alterados
    2. Desempacotamento na função -> passar uma tupla 

## Arrays x Listas

````
A escolha entre listas e arrays depende de necessidades específicas de flexibilidade, desempenho e uso de memória. Para operações gerais e pequenas coleções de dados, listas são frequentemente adequadas. Para grandes volumes de dados numéricos e operações matemáticas mais robustas e intensas, arrays são a melhor escolha.

Grande diferença entre um array e uma lista é como elas se comportam na memória RAM. Enquanto a lista usa ponteiros (o que gasta mais processamento) um array ocupa um lugar fixo na memória tornando o processo mais fácil
````

1. Armazena uma coleção de items, mas item do mesmo tipo -> typecode array('i', [lista])
2. Só aceita valores inteiros, números decimais e caracteres

-- Range uma das melhores maneiras de gera valor, tanto para criar laço de repetição como gerar valores inserido em uma lista e outros tipos de coleções

-- Enumerate - Enumerar elementos de uma coleção (lista, tupla, etc),
Facilita a iteração sobre uma coleção e, simultaneamente, obter o índice do elemento

## Ordenar coleções por propriedades

- Se você quiser ordenar um dict ou tipo de coleção que possui uma chave ou propriedade
- Na tupla e matriz para ordenar se passa o index 

-> from operator import itemgetter

## Map() 

1. Processa e retorna todos os valores

-- Função que recebe uma função e uma coleção de dados e aplica a função a cada elemento da coleção
### Logica mais complexa 
    # verificar a pontuação do aluno no banco de dados
    # verificar se o pagamento foi feito em uma planilha

## Filter 

1. Pode ser usado para processar uma coleção de dados e retornar apenas aqueles dados/ items avalados como verdadeiros

## SET 
 -> recebe valores, não aceita repetição e não tem índice
 -> não é ordenado
 -> não é indexado

