class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def __init__(self):
        self.auto_count += 1
        print(self.auto_count)

    def __add__(self, other):   # Метод, отвечающий за +. Мы перегружаем метод для его использования
        return self.auto_count + other.auto_count

    def __mul__(self, other):   # Метод, отвечающий за умножение
        return self.auto_count * other.auto_count
    
    def __str__(self):
        return 'Будет выводиться сообщение при вызове метода print для объекта класса'


a_1 = Auto()
a_2 = Auto()
a_3 = Auto()
print(a_1)
print(a_1 + a_2)
print(a_1 * a_3)

