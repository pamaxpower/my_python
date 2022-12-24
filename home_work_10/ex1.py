"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ
"""

# взял класс из ДЗ-7 зад.3


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        if wage < 0:
            raise ValueError('Зарплата не может быть отрицательная')
        self._wage = wage

        if bonus < 0:
            raise ValueError('Бонус не может быть отрицательным')
        elif bonus > 50:
            raise ValueError('Размер бонуса не должен превышать 50%')
        self._bonus = int(wage) * int(bonus) / 100

    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, value):
        if value < 0:
            raise ValueError('Зарплата не может быть отрицательная')
        self._wage = value

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if value < 0:
            raise ValueError('Зарплата не может быть отрицательная')
        elif value >= 50:
            raise ValueError('Размер бонуса не должен превышать 50%')
        self._wage = self._wage * value / 100

    
worker1 = Worker('Иван', 'Иванов', 'мастер', 1000, 10)      # все отлично
# worker2 = Worker('Иван', 'Иванов', 'мастер', -1000, 10)     # ошибка: wage < 0
# worker3 = Worker('Иван', 'Иванов', 'мастер', 1000, -5)      # ошибка: bonus < 0
# worker4 = Worker('Иван', 'Иванов', 'мастер', 1000, 51)      # ошибка: bonus > 51

print(f'Зарплата, в руб: {worker1.wage}')
print(f'Премия, в руб: {worker1.bonus}')
