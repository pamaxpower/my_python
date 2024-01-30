'''
Свойства и методы для работы с datetime

'''

from datetime import time, date, datetime, timedelta


d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
                microsecond=24)
delta = timedelta(weeks=53, hours=73, minutes=101,
                seconds=303, milliseconds=60)

print(f'{d.month}')
print(f'{t.second}')
print(f'{dt.hour}')
print(f'{delta.days}')  # -> 374 = 53 * 7 (дни из недель) + 73 / 24 (дни из часов)

# Изменение в datetime
new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)

print(f'{new_dt}\n{one_more_hour}')
