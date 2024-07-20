# How to use a list comprehension in Python

# new_list = [expression for item in iterable]

new_list = [2 * i for i in range(10)]


names = ['João', 'Maria', 'José', 'Pedro', 'Ana', 'Carlos', 'Marta', 'Paulo', 'Lucas', 'Mariana']
aprovados = [f'{name} Aprovado' for name in names]

# Matriz 
from pprint import pprint

pprint([[i for i in range(1, 6)] for x in range(5)])

# List comprehension with condition

# new_list = [expression for item in iterable if condition == True]

new_list1 = [i for i in range(10) if i % 2 == 0]


# Function to check if a number is even
def is_even(x):
    valor = x % 2
    if valor == 0:
        return True
    else:
        return False
    
new_list2 = [i for i in range(10) if is_even(i)]
print(new_list2)

# List comprehension with if else
# new_list = [expression if condition == True else expression2 for item in iterable]


from pprint import pprint as pp
lista = [2 * i for i in range(1,6)]
print(lista)

cores = ['vermelho','azul','verde','amarelo','rosa','preto']
pp([str(cores.index(cor)+1) + ' - ' + cor for cor in cores])

participantes = ['joel','jessica','maria','cris','Larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','maria','cris']

print([i + ' PAGO' if i in pagamento_realizado else i + '' for i in participantes])