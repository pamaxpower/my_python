"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).

Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).

"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": int(wage),
                       "bonus": int(wage) * int(bonus) / 100}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход: {self.income["wage"] + self.income["bonus"]}')


worker1 = Position('Иван', 'Иванов', 'ученик', 10000, 10)
print(f'Имя сотрудника: {worker1.name}')
print(f'Фамилия сотрудника: {worker1.surname}')
print(f'Должность сотрудника: {worker1.position}')
print(f'Размер зарплаты: {worker1.income["wage"]}')
print(f'Бонус к зарплате: {worker1.income["bonus"]}')

worker1.get_full_name()
worker1.get_total_income()

print()

worker2 = Position('Петр', 'Петров', 'мастер', 20000, 30)
worker2.get_full_name()
print(f'Должность сотрудника: {worker2.position}')
worker2.get_total_income()
