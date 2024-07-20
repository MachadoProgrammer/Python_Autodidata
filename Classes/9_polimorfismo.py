# Polimorfismo é a capacidade de se adaptar a diferentes situações, ou seja, a capacidade de um objeto de ser referenciado de várias formas.

class Pessoa:
    # idade e profissao são opcionais
    def apresentar(self, nome, idade=None, profissao=None):
        self.nome = nome

        if idade and profissao != None:
            self.idade = idade
            self.profissao = profissao
            print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.")
        elif idade != None:
            self.idade = idade
            print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos.")
        elif profissao != None:
            self.profissao = profissao
            print(f"Olá, meu nome é {self.nome} e sou {self.profissao}.")
        else:
            print(f"Olá, meu nome é {self.nome}.")
          


pessoa = Pessoa()
pessoa.apresentar("Lucas", 20, "Programador")
pessoa.apresentar("Lucas", 20)
pessoa.apresentar("Lucas", profissao="Programador") 
pessoa.apresentar("Lucas")


class Carro:
    def ligar(self):
        print("Carro ligado.")


class Moto:
    def ligar(self):
        print("Moto ligada.")

def ligar_veiculo(veiculo):
    veiculo.ligar()

carro = Carro()
moto = Moto()

ligar_veiculo(carro)
ligar_veiculo(moto)


