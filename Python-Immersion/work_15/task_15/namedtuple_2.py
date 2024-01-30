'''
При создании класса можно дополнительно передать список значений по умолчанию
Если таких значений меньше, чем в классе, то назначение происходит справа налево

'''

import time
from collections import namedtuple
from datetime import datetime

User = namedtuple('User', ['first_name', 'last_name',
                'birthday'], defaults=['Иванов', datetime.now()])

u_1 = User('Исаак')
print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')

time.sleep(7)

u_2 = User('Галилей', 'Галилео')
print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')

# Время обоих экземпляров совпадает, несмотря на разницу в 7 секунд.
# Значение datatime.now() было вычислено 1 раз при создании класса, 
# и у всех экземпляров оно будет одинаковое, 
# не зависимо от того когда экземпляр был создан 
# (в то же время, спустя несколько секунд или спусть пару дней)