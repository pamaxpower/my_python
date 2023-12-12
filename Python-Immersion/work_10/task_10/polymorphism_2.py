'''
полиморфизм
'''

# нельзя разделить одну строку на другую
path_1 = '/home/user'
path_2 = '/my_project/workdir'
# result = path_1 / path_2    # TypeError: unsupported operand type(s) for /: 'str' and 'str'


# создаем класс для деления строк, наследник от класса str
class DivStr(str):
    def __init__(self, obj):
        self.obj = str(obj)

    # создаем магический метод, отрабатывающий деление строк
    # (срабатывает при символе '/') 
    def __truediv__(self, other):
        # проверяет заканчивается ли первая часть символом '/' (возвращает True/False)
        first = self.obj.endswith('/') 
        start = self.obj
        # проверяем вторую часть
        if isinstance(other, str):
            second = other.startswith('/')
            finish = other 
        elif isinstance(other, DivStr):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)

        # в зависимости от результата возвращаем соответствующий итог
        if first and second:
            return DivStr(start[:-1] + finish)
        if (first and not second) or (not first and second):
            return DivStr(start + finish)
        if not first and not second:
            return DivStr(start + '/' + finish)
        
path_1 = DivStr('/home/user/')
path_2 = DivStr('/my_project/workdir')
result = path_1 / path_2

print(f'{result = }, {type(result)}')
print(f'{result / "text" = }')
print(f'{result / 42 = }')
print(f'{result * 3 = }')
