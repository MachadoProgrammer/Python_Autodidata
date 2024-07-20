
# Função que retorna um valor e será usado depois

def exibir_cotação(moeda):
   if moeda == 'dolar':
      return 5.50
   

cotação = exibir_cotação('dolar')

if cotação > 5:
   print(f'Cotação não está favorável, está em R${cotação}')
else:
    print(f'Cotação está favorável, está em R${cotação}')


# Funções que apenas processa dados 

def exibir_cotação(moeda):
    if moeda == 'dolar':
        print(5.50)

exibir_cotação('dolar')

# Funções que não retornam nada


def exibir_cotação(moeda):
    if moeda == 'dolar':
        print(5.50)
        return
    
cotação = exibir_cotação('dolar')