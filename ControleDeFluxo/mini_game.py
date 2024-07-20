# Turtle -> fazer desenhos na tela com o python 
from turtle import Turtle
# Iniciar uma turtle
t = Turtle()
# Definir a velocidade da turtle
t.speed(1)

# CLEAN CODE NA PRÁTICA
# Uma função para cada probleminha
def obter_distancia():
    distancia = int(
        input('Quantos pixels devemos movimentar para a frente?'))
    return distancia
def rotacionar_turtle(turtle):
    movimentar_para_lado = input(
            'Rotacionar para d:direta, e:esquerda n:não rotacionar')
    if movimentar_para_lado == 'd':
        rotacionar_direita(turtle)
    elif movimentar_para_lado == 'e':
        rotacionar_esquerda(turtle)
def rotacionar_direita(turtle):
    angulo = int(input('Quanto para a direta devemos rotacionar?'))
    t.right(angulo)
def rotacionar_esquerda(turtle):
    angulo = int(input('Quanto para a esquerda devemos rotacionar?'))
    t.left(angulo)

t = Turtle()
while True:
    direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás"')
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distancia)
    resposta = input('Continuar andando?')
    if resposta not in ('sim', 's'):
        break

    input()

    # # Movimentar a turtle para a posição (x, y)
    # t.goto(100, 100)
    # # Fechar a janela
    # t.done()