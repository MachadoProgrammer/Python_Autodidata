# Usuario tentando fazer uma compra na internet e a internet caiu
# finally vai desfazer a compra 

internet = None
try:
    print("Conectando..." + internet)
except Exception as e:
    print('Erro: ', e)
finally:
    # finally é executado sempre, independente de erro ou não
    print('Desconectando...')
    

