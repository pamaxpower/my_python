'''
Задание №4

Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.

У сотрудника должен быть:

шестизначный идентификационный номер
уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
'''
from random import randint
from task_3 import Info


# class Info():
#     def __init__(self, lastname, name, surname, age):
#         self.name = name
#         self.lastname = lastname
#         self.surname = surname
#         self.__age = age

#     def birthday(self):
#         return (self.__age + 1)

#     def full_name(self):
#         return f'Полное имя: {self.lastname} {self.name} {self.surname}'
    

class Employee(Info):
    def __init__(self, lastname, name, surname, age):
        super().__init__(lastname, name, surname, age)
        self.__employee_id = randint(100000, 999999)
        self.__level = sum(int(i) for i in str(self.__employee_id)) % 7
        
    def get_id(self):
        return self.__employee_id

    def get_level(self):
        return self.__level

e1 = Employee('Иванов', 'Иван', 'Иванович', 30)
print(e1.get_id())
print(e1.get_level())

