'''
Модуль datetime
- модуль для работы даты и времени
- имеется модуль zoneinfo для работы с часовыми поясами

Создание даты и времени
'''

from datetime import time, date, datetime

# дата в календаре от 01.01.0001 до 31.12.9999
d = date(year=2007, month=6, day=15)

t = time(hour=2, minute=14, second=0, microsecond=24)

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
second=0, microsecond=24)

print(f'{d = }\t-\t{d}')
print(f'{t = }\t-\t{t}')
print(f'{dt = }\t-\t{dt}')
