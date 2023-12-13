'''
В метод можно передавать не только аргументы, 
но даже экземпляр класса
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

    # метод меняет здоровье у персонажа:
    # Прибавляет значение к self и отнимает у 
    # переданного экзмемпляра other  
    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.health = }, {p2.health = }, {p3.health = }')

# так как метод вызывает у экземпляра p1, его здоровье будет увеличено на 10,
# в свою очеред здоровье переданного экземпляра p2 будет уменьшено 
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
