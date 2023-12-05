'''
Замыкание изменяемых объектов (типа list)
'''

from typing import Callable

# в тело внешней функции добавляем пустой список

def add_one_str(a: str) -> Callable[[str], str]:
    names = []
    def add_two_str(b: str) -> str:
        names.append(b)         # список накапливает значения
        return a + ', ' + ', '.join(names)
    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex'))        # -> Hello, Alex
print(hello('Karina'))      # -> Hello, Alex, Karina (тк в списке уже 2 значения)
print(bye('Alina'))         # -> Good bye, Alina (а это уже другой экземпляр, поэтому и список будет другой)
print(hello('John'))        # -> Hello, Alex, Karina, John
print(bye('Neo'))           # -> Good bye, Alina, Neo