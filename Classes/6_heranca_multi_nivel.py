class Usuario:
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao

    def registrar(self):
        print(f"Usuário {self.nome} registrado com sucesso!")


class Gestor(Usuario):
    def __init__(self, nome, salario, profissao, setor):
        super().__init__(nome, salario, profissao)
        self.setor = setor

    def definir_setor(self, setor):
        print(f"Setor {setor} definido com sucesso!")


usuario1 = Usuario("João", 2000, "Analista de Sistemas")
gestor = Gestor("Maria", 5000, "Gerente de Projetos", "TI")

# Evitar a herança multi-nível
# A herança multi-nível pode tornar o código complexo e difícil de manter

# Herança multipla

class Pessoa:
    nome = 'Sou uma pessoa'

class Profissinal:
    nome = 'Sou um profissional'

class AtorProfissional(Pessoa, Profissinal):
    pass 

print(AtorProfissional.mro()) # MRO - Method Resolution Order 

# 