'''
Замыкание неизменяемых объектов (типа str)
'''

from typing import Callable

# теперь во внешнюю функцию добавляем пустую строку
# а во внутренню добавляем nonlocal text (указываем внутренней 
# функции, что переменная text не какая-то внутренняя переменная,
# а находится на уровень выше, вне этой функции)
def add_one_str(a: str) -> Callable[[str], str]:
    text = ''
    def add_two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text
    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

# результаты получаются аналогичные предыдущему примеру
print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
