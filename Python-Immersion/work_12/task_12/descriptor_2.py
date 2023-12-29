'''
Напишем класс, который хранит имя ученика, его возраст, номер класса (от 1 до 11)
и номер кабинета, в котором сидит класс.

'''

class Student:
    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'

std1 = Student('Шурик', 7, 1, 12)
print(std1)

# если внимательно рассмотреть код, можно увидеть несколько недочетов: все параметры могут принимать любые значения (даже отрицательные), НО

# * возраст не может быть меньшим нуля, т.е. должно быть ограничение age > 0
# * классов в школе 11  ->  1 <= grade <= 11
# * да и номера кабинетов не бесконечны. Пусть будет  3 <= office <= 42

# чтобы выйти из этой ситуаци можно прописать геттер, сеттер и делейтер для всех этих значений, 
# но это будет слишком много кода

# либо можно написать дескриптор для проверки всех трех свойств на заданный диапазон

