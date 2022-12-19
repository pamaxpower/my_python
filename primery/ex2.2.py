class Road():

    # Вес асфальта в тоннах для 1 кв.м. полотна толщиной в 1 см
    # Определяю его как private из соображений, что это константа, не подлежащая изменению
    __weight = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Создан новый объект класса Road длиной {self._length} метров и шириной {self._width} метров')

    def get_weight(self, thickness):
        ret_val = self._length * self._width * thickness * self.__weight / 1000
        print(f'Вес асфальта, требуемый для укладки полотна толщиной {thickness} см, равен {ret_val} т')

        return ret_val

r1 = Road(5000, 20)
w1 = r1.get_weight(5)

# r2 = Road(1000, 20)
# w2 = r2.get_weight(20)

#print(f'Суммарный вес асфальта для двух объектов = {w1 + w2}')