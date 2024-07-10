#### dates ######
from datetime import datetime

now = datetime.now() # iniciar la hora
print(now.hour)
print(now.day)
print(now.month)
print(now.minute)
print(now.second)
print(now.year)

timestamp = now.timestamp()
print(timestamp)

year_2024 = datetime(2024, 7, 9, 22, 8, 00) # año, mes, dia, hora, minitos, segundosS
print(year_2024)

from datetime import time

current_time = time(22, 18, 00)
print(current_time)

from datetime import date
current_date = date(2024, 7, 9)
# current_date = date.today() # para iniciarlo
print(current_date.weekday())
print(current_date.day)
print(current_date.month)
print(current_date.year)

from datetime import timedelta
init = timedelta(220, 100, 100, weeks=50) # diferencia de dias, trabajar con franjas de fechas
print(init)
init2 = timedelta(5,0,2)
init3 = timedelta(22, 6, 0)
print(init3 - init2)
