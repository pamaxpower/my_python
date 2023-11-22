"""
Задача 2.

Напишите функцию, которая генерирует
псевдоимена.

Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.

Полученные имена сохраните в файл.
"""
from random import randint, choices

VOWELS = 'аеиоуыэюя'  # гласные русские буквы
ALPHABET = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1)])

def generation_name(count):
    i = 0
    name = ""
    while i != count:
        word = choices(ALPHABET, k=randint(4, 7))
        if any(item in VOWELS for item in word):
            name += ''.join(word).capitalize() + '\n'
            i += 1
    with open('task7_2.txt', 'a', encoding='utf-8') as f:
        f.write(name)


generation_name(6)