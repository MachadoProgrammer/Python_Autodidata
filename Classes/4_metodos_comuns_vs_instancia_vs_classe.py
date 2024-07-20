# Metodos comuns
# Metodos de Classe(Class Methods)
# Metodos estaticos(Static Methods)

# Metodos comuns
# -> São métodos que utilizam o parâmetro self e são utilizados para acessar os atributos e métodos do objeto

# Metodos de Classe(Class Methods)
# -> São métodos que utilizam o parâmetro cls e são utilizados para acessar os atributos e métodos da classe
# -> cls = passa a classe inteira como parâmetro e nao a instancia

class Computador:
    sistema_operacional = 'Windows 10'  # variável de classe

    # variáveis de classe são compartilhadas por todos os objetos da classe

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca  # variável de instância
        # variáveis de instância são específicas para cada objeto da classe
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('HP', memoria_ram, 'Onboard')

    @classmethod
    def computador_gamer(cls, memoria_ram):
        return cls('Alienware', memoria_ram, 'GTX 1080TI')

    def ExibirInformacoes(self):
        print(f'Marca: {self.marca}, Memória RAM: {self.memoria_ram}, Placa de vídeo: {self.placa_de_video}')

    @staticmethod
    def roda_programas(memoria_ram):
        if memoria_ram < 8:
            print('Computador não é adequado para rodar programas pesados')
        else:
            print('Computador é adequado para rodar programas pesados')


# configuracao p/ cliente de escritorio
Computador.computador_escritorio('8GB').ExibirInformacoes()

# configuracao p/ clientes de trabalho pesado
Computador.computador_gamer('16GB').ExibirInformacoes()

# Metodos estaticos(Static Methods)
# -> São métodos que não utilizam o parâmetro self ou cls e não acessam atributos ou métodos da classe
# -> São métodos que não dependem de instâncias ou da classe

Computador.roda_programas(4)  # Computador não é adequado para rodar programas pesados
