"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ
"""


class Grade:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if not (1 <= value <= 5):
            raise ValueError('Оценка должна быть от 1 до 5')
        self.my_attr = value

# Написал новый класс


class Exam:
    score = Grade('score')

    def __init__(self, score):
        self.score = score


ex1 = Exam(3)       # все ок
# ex2 = Exam(-2)      # ошибка: оценка < 1 
ex3 = Exam(1)       # все ок
ex4 = Exam(5)       # все ок
# ex5 = Exam(10)      # ошибка: оценка > 5
