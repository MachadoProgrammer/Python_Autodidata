# Funções com n° de argumentos nomeados dinâmicos = **kwargs
# **kwargs -> recebe um dicionário com todos os argumentos nomeados passados
def concatenar(**kwargs):
    print(kwargs)
    print(kwargs['nome'] + ' ' + kwargs['sobrenome'])

concatenar(nome='João', sobrenome='Silva') # Os argumentos nomeados são passados como um dicionário

def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for key in kwargs.values():
        print(key)
        
#         Posicional, Posicionais(args),Nomeados(kwargs
fazer_calculo('João', 1, 2, 3, 4, 5, a=6, b=7, c=8) # Os argumentos nomeados são passados como um dicionário