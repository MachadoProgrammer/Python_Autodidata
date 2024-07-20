# logging
# https://docs.python.org/3/library/logging.html

import logging as lg

log = lg.getLogger(__name__)

# Níveis de log
'''
debug -> São informações que são úteis para desenvolvedores
info -> São informações que são úteis para usuários, mas nao é um erro
warning -> quero que o usuário saiba que algo deu errado, mas não é um erro mas futuramente pode ser
error -> É um erro, mas não é um erro critico
critical -> É um erro critico, que pode parar a aplicação
'''

# A informação que estou guardado, qual o nivel de impacto que ela tem na aplicação
# o modulo logging só vai mostrar as informações do nivel warning para cima

lg.basicConfig(level=lg.DEBUG, filename='app.log', filemode='a',
               format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Configuração do log

lg.critical('Critical')
lg.error('Error')
lg.warning('Warning')
lg.info('Info')
lg.debug('Debug')
