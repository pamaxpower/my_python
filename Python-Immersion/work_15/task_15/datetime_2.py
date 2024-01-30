'''
Разница времени
- разница во времени между различными датами и временными промежутками

● days — хранит переданные дни. Недели преобразуются в 7 дней
● seconds — хранит секунды. Минуты превращаются в 60 секунд, а часы в 3600
секунд
● microseconds — хранит микросекунды

'''

from datetime import timedelta

delta = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5,
milliseconds=6, microseconds=7)
print(f'{delta = }\t-\t{delta}')

delta1 = timedelta(weeks=53, days=500, hours=73, minutes=101,
seconds=303, milliseconds=67890,
microseconds=1234567)

# при отрицательных значениях с минусами хранятся только дни, время остается положительным
neg_delta = timedelta(days=-3, minutes=-42)

print(f'{delta1 = }\t-\t{delta1}')
print(f'{neg_delta = }\t-\t{neg_delta}')

