'''
Множественного наследование

- любой класс в Python может являться наследником сразу у нескольких классов
Напрмер, наследуя от классов Птицы или Рыбы, класс Существо позволит 
создать летающую рыбу или плавающую птицу

'''

from inheritance_2 import Person

# создаем класс адрес
class Address:
    def __init__(self, country, city, street):
        self.country = country or ''
        self.city = city or ''
        self.street = street or ''

    def say_address(self):
        return f'Адрес героя: {self.country}, {self.city}, {self.street}'

# создаем класс оружия
class Weapon:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand or 'Клинок'
        self.right_hand = right_hand or 'Лук'

# теперь класс Hero наследуется от 3х классов
# в скобках указываются родительские классы (по приоритету)
class Hero(Person, Address, Weapon):
    def __init__(self, power, name=None, race=None, speed=None, 
                 country=None, city=None, street=None, left_hand=None, 
                 right_hand=None):
        self.power = power
        # нельзя использовать функцию super()? nr она будет обращаться только к первому родительскому классу
        # в таком случае надо у каждого родительского класса вызвать свой метод
        # но это тоже не лучшая запись
        Person.__init__(self, name, race, speed)
        Address.__init__(self, country, city, street)
        Weapon.__init__(self, left_hand, right_hand)

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2

    def add_many_ups(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)


p1 = Hero('archery', 'Сильвана', 'Эльф', 120,
            country='Эльфляндия', street='Ночного эльфа',
            left_hand='Стрела')

print(f'{p1.say_address()}')
print(f'{p1.right_hand = }, {p1.left_hand = }')
