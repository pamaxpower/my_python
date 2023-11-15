'''
Модуль random

.
● randint(a, b) — целое числа в диапазоне [a, b].

● uniform(a, b) — вещественное числа в диапазоне от a до b. 
Правая граница может как входить, так и не входить в 
возвращаемый диапазон. Зависит от способа округления.

● choice(seq) — возвращает случайный элемент из непустой
последовательности.

● randrange(stop) или randrange(start, stop[, step]) 
работает как вложение функции range в функцию choice, 
т.е. choice(range(start, stop, step)). 
Возвращает случайное число от start до stop с шагом step.

● shuffle(x) — перемешивает случайным образом изменяемую
последовательность, не создавая новую.

● sample(population, k, *, counts=None) — выбирает k уникальных 
элементов из последовательности population и возвращает 
их в новой последовательности.
Параметр counts позволяет указать количество повторов элемента.
'''
import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(f'{rnd.randint(START, STOP) = }')
print(f'{rnd.uniform(START, STOP) = }')
print(f'{rnd.choice(data) = }')
print(f'{rnd.randrange(START, STOP, STEP) = }')

print()
 
print(f'{data = }')
rnd.shuffle(data)
print(f'{data = }')
print(f'{rnd.sample(data, 2) = }')
print(f'{rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100]) = }')
# будет рассматривать список, где первые 5 элементов содержатся 1 раз, а последний 100

