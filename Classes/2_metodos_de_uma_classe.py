class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou desligando')

    def ExibirInformacoes(self):
        print(f'Marca: {self.marca}, Memória RAM: {self.memoria_ram}, Placa de vídeo: {self.placa_de_video}')

# self é uma referência ao próprio objeto que está sendo instanciado e é passado automaticamente para todos os métodos da classe
# e é utilizado para acessar os atributos e métodos do objeto 

computador1 = Computador('Asus', '8GB', 'GTX 1050')
computador1.Ligar()
computador1.ExibirInformacoes()
computador1.Desligar()
