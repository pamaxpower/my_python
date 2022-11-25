""" Пользователь вводит время в секундах. Переведите время в часы, минуты и
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

time = int(input('Введите время в секундах: '))
hour = time // 3600
minute = (time - hour*3600) // 60               # (time % 3600) // 60
second = time - hour*3600 - minute*60           # time % 60
print(f'{hour}:{minute}:{second}') 


sec = time
hou = sec / 3600
minu = sec / 60
print(f'Время {hou:.5f} : {minu} : {sec}')
