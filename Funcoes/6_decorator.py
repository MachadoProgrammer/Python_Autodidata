def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
  
  
def upper_case_decorator(function):
  def wrapper():
      func = function()
      make_upper = func.upper()
      return make_upper
  return wrapper


def split_decorator(function):
  def wrapper():
      func = function()
      make_split = func.split()
      return make_split
  return wrapper

# @my_decorator
# def my_function():
#     print("Dentro da função")
    
# my_function()

# EXAMPLE 2

@upper_case_decorator
def text():
    return "texto dentro da função"


print(text())

# EXAMPLE 3

@split_decorator
@upper_case_decorator
def text1():
    return "texto dentro da função"

print(text1())

# DESAFIO
'''
Crie um decorator que irá pegar a função que for passado para ele e imprimir o horário atual
antes e depois de executar a função.
'''

from datetime import datetime

def hora_decorator(func):
    def wrapper():
        print(datetime.now())
        func()
        print(datetime.now())
    return wrapper

@hora_decorator
def my_function():
    print("Dentro da função")

my_function()