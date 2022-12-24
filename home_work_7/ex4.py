"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
 speed, color, name, is_police (булево).

А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print(f'Машина едет')

    def car_stop(self):
        print(f'Машина остановилась/стоит')

    def car_turn(self, turn):
        """
        Функция определяет куда повернула машина
        :param turn: целое число
        :return: показывает куда повернула машина
        """
        if turn % 2 == 0:
            print(f'Машина повернула налево')
        else:
            print(f'Машина повернула направо')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'\t!!!Вы превысили скорость!!!')
        else:
            print('Скорость в пределах нормы')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'\t!!!Вы превысили скорость!!!')
        else:
            print('Скорость в пределах нормы')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


car1 = TownCar(65, 'red', 'mazda', False)
car2 = SportCar(120, 'green', 'bmw', False)
car3 = WorkCar(39, 'orange', 'kamaz', False)
car4 = PoliceCar(10, 'white', 'toyota', True)
car5 = Car(65, 'red', 'mazda')

exit()
print(car1.color)
print(car2.speed)
print(car3.name)
print(f'Машина полицейская? {car2.is_police}')
print(f'Машина полицейская? {car4.is_police}')
print()
car2.car_go()
car2.car_turn(2)
car2.car_turn(5)
car2.car_stop()
print()
car3.show_speed()
car1.show_speed()
car1.speed = 59
car1.show_speed()
