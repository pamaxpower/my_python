'''
Модуль random

- используется для генерации псевдослучайных чисел

* random() - генерирует псевдослучайные числа в диапазоне от 
нуля включительно до единицы исключительно — [0, 1).
● seed(a=None, version=2) — инициализирует генератор. Если значение a не
указано, для инициализации используется текущее время ПК.
● getstate() — возвращает объект с текущим состоянием генератора.
● setstate(state) — устанавливает новое состоянии генератора, принимая на
вход объект, возвращаемый функцией getstate

'''
import random as rnd


print(f'{rnd.random() = }')
rnd.seed()
state = rnd.getstate()
print(f'{state = }')
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
rnd.setstate(state)
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')

