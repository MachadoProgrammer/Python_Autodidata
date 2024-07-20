import logging as lg

log = lg.getLogger(__name__)

lg.basicConfig(level=lg.DEBUG,filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %('
                                                                       'message)s')  # Configuração do log
try:
  email = input('Digite seu email: ')
  senha_bancaria = int(input('Digite sua senha bancária: '))

  if senha_bancaria == 1234:
      print(f'{email} entrou no sistema')
      log.info(f'{email} entrou no sistema')


except ValueError as e:
  log.error(f'Erro: {type(e).__name__} - {e}')
  print('Digite apenas números na senha bancária')