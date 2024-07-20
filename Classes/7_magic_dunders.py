# Métodos mágicos são métodos especiais que tem dois underlines antes e depois do nome.
# __init__ é um exemplo de método mágico.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.habilidades = ['Habilidade 1', 'Habilidade 2', 'Habilidade 3']

    # repr é um método mágico que retorna uma representação do objeto repr(objeto)
    def __repr__(self) -> str:
        return f'Pessoa({self.nome}, {self.idade})'

    # len é um método mágico que retorna o tamanho do objeto len(objeto)
    def __len__(self):
        # Retorna o tamanho da lista de habilidades
        return len(self.habilidades)
    
    def __str__(self) -> str:
        return f'{self.nome} com as habilidades: {self.habilidades}'
    


print(dir(Pessoa))