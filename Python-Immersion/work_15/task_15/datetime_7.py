'''
Проверка

Что выведет программа
'''

from datetime import datetime, timedelta


d = datetime.now()          # время сейчас

td = timedelta(hours=1)     # разница 1 час (3600)
for i in range(24*7):
    if d.weekday() == 6:    # если сейчас вскр, то выйти
        break
    else:                   # если нет, то прибавить 1 час
        d = d + td

print(i)        # покажет через сколько часов будет вскр
