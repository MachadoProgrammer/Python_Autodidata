try:
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(meses[15])
except IndexError as e:
    print(f'FAVOR DIGITAR UM NÚMERO ENTRE 0 E {len(meses) - 1}')
    # ver exatamente qual é o erro
    print(f'{type(e).__name__}: {e}')

# Guarda info de erros usando logging

# Pesquise sobre a exceção
# Encontrar os erros específicos e corrigi-los mas o usuário não precisa ver
# o usuario deve receber uma mensagem mais amigável com instruções claras de o que ele deve fazer
# quando algo foi feito de forma errada ou quando algum tipo de erro foi encontrado na sua aplicação
