# Classe abstrata é uma classe que não pode ser instanciada, mas pode ser herdada
# Cria um contrato(esqueleto) que deve ser implementado pelas classes filhas

from abc import ABC, abstractmethod


class Carro(ABC):
    @abstractmethod
    def exibir_informacoes(self):
        pass
    

class Gol(Carro):
    def exibir_informacoes(self):
        print('Marca: Volkswagen\nModelo: Gol\nAno: 2020\nCor: Branco')