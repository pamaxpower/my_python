"""Простой класс с атрибутами и методом"""


class Worker:
    """Класс-работник"""
    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_profit(self):
        """Расчет зарплаты"""
        return self.hours * self.rate


OBJ = Worker('Иван', 'Иванов', 10, -100)
print(OBJ.total_profit())

OBJ.hours = 20
OBJ.rate = 200
print(OBJ.total_profit())

# теперь попробуем присвоить какому-либо из атрибутов отрицательное значение
