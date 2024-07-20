tentativas = 0
while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == "123":
        print("Acesso permitido")
        break
    else:
        tentativas += 1
        print("Senha incorreta")

# 