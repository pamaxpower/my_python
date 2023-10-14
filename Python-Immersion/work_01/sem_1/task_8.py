"""
Задание №8
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
 *
 ***
 *****
 *******
*********
"""

row = int(input('Введите количество рядов елки: '))
space = ' '
symbol = '*'

for i in range(row+1):
    print(space*(row-i) + symbol*(2*i-1) + space*(row-i))


'''
space = ' '
symbol = '*'

rows = int(input("Введите количество рядов: "))
spaces = rows - 1
symbols = 1

for i in range(rows):
    print(
        (space * spaces) +
        (symbol * symbols) +
        (space * spaces)
    )
    symbols += 2
    spaces -= 1
'''