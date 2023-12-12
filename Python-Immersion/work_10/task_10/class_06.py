'''
Конструктор экземпляра

__init__ - магический метод __init__ срабатывает при каждом вызове экземпляра

class Person:
    ...
    def __init__(self):
        ...

1) Первый параметр функции __init__ - всегда self
2) Параметры метода __init__ попадают в экземпляр 
класса при его создании 
3) обращение к атрибутам происходит через self.name

Параметр self:
В работе с классами self является указателем на тот экземпляр класса, 
к которому происходит обращение. Например для p1 это p1.level = 1. 
Какое бы имя вы не дали экземпляру, self подставляет его на своё место.
'''

class Person:
    max_up = 3

    def __init__(self):
        self.level = 1
        self.health = 100

    
p1 = Person()
p2 = Person()

print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# print(f'{Person.max_up = }, {Person.level = }, {Person.health =}') # AttributeError: type object 'Person' has no attribute 'level'

# при определении атрибута level у класса, мы не меняем значения у экземпляров.
# это разные объекты , в разных областях видимости 
Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')
