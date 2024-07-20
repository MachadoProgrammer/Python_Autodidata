# São valores que você quer que exista dentro do código, mas que não quer que fique exposto.
# Usando como chave de API, senha de banco de dados, etc.
# pip install python-dotenv

import os 
from dotenv import load_dotenv

load_dotenv()

usuario = os.environ['USUARIO']
print(usuario)