"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ
"""


class MyDesciptor:

    def __set__(self, instance, value):
        if not isinstance(value, str):          # если value не строка
            raise ValueError("Должен быть текст")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


# взял класс из ДЗ-7 зад.4
class Car:
    color = MyDesciptor()
    name = MyDesciptor()

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


car1 = Car(60, 'red', 'mazda')  # все ок
# car2 = Car(60, 10, 'mazda')     # ошибка: color не str
# car3 = Car(60, 'red', 30)       # ошибка: name не str

print(car1.color)
# car1.color = 20     # ошибка: color не str
print(car1.name)
