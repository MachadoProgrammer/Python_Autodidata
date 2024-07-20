class Computador:
    sistema_operacional = 'Windows 10' # variável de classe
    # variáveis de classe são compartilhadas por todos os objetos da classe

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca # variável de instância
        # variáveis de instância são específicas para cada objeto da classe
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou desligando')

    def ExibirInformacoes(self):
        print(f'Marca: {self.marca}, Memória RAM: {self.memoria_ram}, Placa de vídeo: {self.placa_de_video}')


print(Computador.sistema_operacional) # Windows 10