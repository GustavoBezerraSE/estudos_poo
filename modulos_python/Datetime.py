#https://docs.python.org/2/library/datetime.html
from datetime import datetime, timedelta
from locale import  setlocale, LC_ALL

"""
data = datetime(2022, 6, 6, 10, 2, 53)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data1 = datetime.strptime('06/06/2022 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data1 + timedelta(days=5, seconds=59)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data2 = datetime.strptime('11/06/2022 20:20:00', '%d/%m/%Y %H:%M:%S')
dif = data2 - data1
print(dif.days)
"""

setlocale(LC_ALL, 'pt-br.utf-8')

dt = datetime.now()
formatacao = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao)
print(formatacao2)

