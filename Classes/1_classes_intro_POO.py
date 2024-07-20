# Classe

class Computador:
    def __init__(self, brand, memory, gpu):
        self.brand = brand
        self.memory = memory
        self.gpu = gpu


computador1 = Computador('Asus', '8bg', 'Nvidia')
print(computador1.memory)
print(computador1.brand)
print(computador1.gpu)
