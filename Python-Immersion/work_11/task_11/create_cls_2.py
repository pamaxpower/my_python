'''
Контроль создания класса через __new__

- срабатывает раньше __init__ и определяет, что должен вернуть класс 
в качестве себя - класса
'''

class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Создал класс {cls}')
        return instance

print('Создаём первый раз')
u_1 = User('Спенглер')

print('Создаём второй раз')
u_2 = User('Венкман')

print('Создаём третий раз')
u_3 = User(name='Стэнц')
