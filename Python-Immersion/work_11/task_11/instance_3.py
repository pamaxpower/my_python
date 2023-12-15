'''
Представление для создания экземпляра

Дандер __repr__ предназначен для вывода информации программисту
- аналогичен __str__ 

Общий вид:
class Person():
    ...

    def __str__(self):
        ...
        return f'Person({self.param})'

'''

class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __repr__(self):
        return f'User({self.name})'

user = User('Спенглер')
print(user)

# Если скопировать вывод метода repr и присвоить его переменной,
# должен получится ещё один экземпляр класса