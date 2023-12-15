'''
Представление экземпляра
- работа функции print()

'''

class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
    def simple_method(self):

        """Example of a simple method."""
        self.name.capitalize()

# создаем экземпляр класса
user = User('Спенглер')

# пытаемся вывести его на печть
print(user)     # -> <__main__.User object at 0x0000026E35E59F90>

# в результате получаем информацию о том, что код был запущен из модуля __main__ и адрес объекта в оперативной памяти
