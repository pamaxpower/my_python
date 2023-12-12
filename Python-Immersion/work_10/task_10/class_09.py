'''
Методы класса
- функции внутри класса

- для доступа к методу применяют точечную нотацию и круглые скобки
ClassName.method - доступ к атрибуту класса
ClassName.method() - доступ к методу класса

- метод, как и функция, может принимать аргументы
ClassName.method(*args, **kwargs)
'''

class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.level = }, {p2.level = }, {p3.level = }')

p3.level_up()
p1.level_up()
p3.level_up()
print(f'{p1.level = }, {p2.level = }, {p3.level = }')