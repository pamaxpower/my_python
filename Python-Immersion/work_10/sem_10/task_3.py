'''
Задание №3

Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
'''

class Info():
    def __init__(self, lastname, name, surname, age):
        self.name = name
        self.lastname = lastname
        self.surname = surname
        self.__age = age

    def birthday(self):
        return (self.__age + 1)

    def full_name(self):
        return f'Полное имя: {self.lastname} {self.name} {self.surname}'
    
n1 = Info('Иванов', 'Иван', 'Иванович', 30)
print(n1.birthday())
print(n1.full_name())
n1.__age = 50
print(n1.__age)