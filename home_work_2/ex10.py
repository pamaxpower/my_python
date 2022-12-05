'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.

Реализуйте алгоритм перемешивания списка.

при N = 10: список из 10 элементов , где каждый элемент рандромное числов диапазоне от -10 до 10

'''
import random

num = int(input())
listInt = []
for i in range(num):
    listInt.append(random.randint(-num, num))

print(listInt)   

position = ''

with open('text.txt', 'r') as data:
    position = data.read().split('\n')
    print(position)

print(
    f'Произведение {int(position[0])} и {int(position[1])} '
    + f'элементов равно: {listInt[int(position[0])]*listInt[int(position[1])]}')