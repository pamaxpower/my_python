"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

s = [b'class', b'function', b'method']
for el in s:
    print(f'Тип переменной: {type(el)} \t Значение: {el} \t Длина: {len(el)}')
