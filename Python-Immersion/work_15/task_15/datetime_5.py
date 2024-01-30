'''
Вывод по формату:

dt.timestamp() - относительно начала времен в Python
dt.isoformat() - вывод в официальном формате
dt.strftime(FORMAT) - вывод строки по формату время
%d - число дата
%B - месяц в виде текста (%B - полностью, %b - сокращенно)
%Y - год в виде 4 цифр
%A - день недели
%H:%M:%S - время
%W - номер недели от начала года
%j - день от начала года

'''

from datetime import datetime


dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
microsecond=24)
print(dt)
print(dt.timestamp())       
print(dt.isoformat())       
print(dt.weekday())         # номер дня недели (от 0-пн до 6-вскр)

print(dt.strftime('Дата  День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))


