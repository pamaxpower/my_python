class ParentClass:
   def __init__(self):
       print("Конструктор класса-родителя")

   def my_method(self):
       print("Метод my_method() класса ParentClass")


class ChildClass(ParentClass):
   def __init__(self):
       print("Конструктор дочернего класса")
       super().__init__()

   def my_method(self):
       print("Метод my_method() класса ChildClass")
       super().my_method()
       self.a = 1


c = ChildClass()
c.my_method()

"""
Конструктор дочернего класса
Конструктор класса-родителя
Метод my_method() класса ChildClass
Метод my_method() класса ParentClass
"""
