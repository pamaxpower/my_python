'''
Декоратор @property

class Name:
    ...
        @property
        def param(self):
            ...
            return ...

        
'''
class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

user = User('Стивен')
print(f'{user.name = }')
user.name = 'Славик' # AttributeError: can't set attribute 'name'

# класс User получает имя name и сохраняет его в 
# защищенной переменной _name (мы не можем обратиться к ней вне класса)

# - для получения значения -name мы создаем метод, который возвращает имя пользователя
# - при попытке изменить имя - получаем ошибку, т.к. _name это getter (только для чтения)


