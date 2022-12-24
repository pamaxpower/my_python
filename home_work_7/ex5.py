"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).

Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.

Создать экземпляры классов и проверить, что выведет описанный метод для
каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print("Запуск отрисовки\n")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Я пишу ручкой\n")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Я рисую карандашом\n")


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Я черчу маркером\n")


item1 = Stationery('')
item1.draw()
item1 = Pen('Ручка')
item1.draw()
item1 = Pencil('Карандаш')
item1.draw()
item1 = Handle('Маркер')
item1.draw()
