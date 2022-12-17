"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).

Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна. 
Использовать формулу: длина*ширина*масса асфальта для
покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины
полотна.

Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    __asphalt_weigth = 25  # масса асфальта на 1кв.м дороги
    __layer_heigth = 5  # высота слоя асфальта в см

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'\nСоздан объект дорога {self._length}x{self._width} м')

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.__asphalt_weigth \
                       * self.__layer_heigth / 1000
        print(f'Для укладки асфальтом данного участка дороги нужно '
              f'{asphalt_mass} тонн асфальта')


road1 = Road(5000, 20)
road1.asphalt_mass()

road2 = Road(777, 15)
road2.asphalt_mass()
road2._length = 1777  # поменяли длину дороги
road2.asphalt_mass()  # изменилось кол-во асфальта