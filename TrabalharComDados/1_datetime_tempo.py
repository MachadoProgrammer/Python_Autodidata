# datetome(ano, mes, dia, hora, minuto, segundo, microsegundo)
# datetime.strptime(data, formato)
# datetime.now()
# datetime.fromtimestamp(timestamp)
from datetime import datetime
from dateutil.relativedelta import relativedelta

data = datetime(2025,5,15) 

# strftime() - datetime para string
data_str = data.strftime('%d/%m/%Y')

# strptime() - string para datetime
data = datetime.strptime('15/05/2025', '%d/%m/%Y')

# datetime.now() - data e hora atual
# datetime.today() - data e hora atual
data_hora_atual = datetime.now()

# relativedelta - adicionar ou subtrair dias, meses, anos, horas, minutos, segundos e microsegundos
# e ver a diferença entre duas datas
data_mais_30_dias = data + relativedelta(days=30)
data_menos_30_dias = data - relativedelta(days=30)

# timestamp - segundos desde 01/01/1970
timestamp = data.timestamp()
print(timestamp)

data_birthday = data - datetime.now()
print(data_birthday.days)