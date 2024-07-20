class Camera: # (object) -> herdamos as propriedades de object
              # F12 -> abrir a documentação da classe
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(f"{self.modelo} tirando foto...")

# Herança -> criar funcionalidades similares dentro do código ou expandir funcionalidades existentes

class CameraDigital(Camera): # Herdamos as propriedades da classe Camera
    def __init__(self, marca, megapixels, modelo):
        super().__init__(marca, megapixels) # super() -> chama o construtor da classe pai
        self.modelo = modelo

    def gravar_video(self):
        print(f"{self.modelo} gravando vídeo...")
    
    def tirar_foto(self):
        print(f"{self.modelo} tirando foto... modelo: {self.modelo}")

class CameraSeguranca(Camera):
    def __init__(self, marca, megapixels, resolucao):
        super().__init__(marca, megapixels)
        self.resolucao = resolucao

    def resolucao_(self):
        print(f"Gravando vídeo em {self.resolucao}...")

cam = CameraDigital("Canon", 24, "EOS 80D")
cam.gravar_video()
cam.tirar_foto()

cam_seg = CameraSeguranca("Sony", 12, "1080p")
cam_seg.resolucao_()


print(issubclass(CameraDigital, Camera)) # True
print(issubclass(CameraSeguranca, Camera)) # True

# Possibilidade de sobrescrever métodos da classe pai
# Modificar como o método tirar_foto() funciona
