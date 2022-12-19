"""__eq__"""


class MyClass:
    def __init__(self):
        self.x = 40

    def __eq__(self, y):
        print(y)
        return self.x == y


mc = MyClass()
print("Равно" if mc == 40 else "Не равно")
print("Равно" if mc == 41 else "Не равно")

"""
Равно
Не равно
"""
