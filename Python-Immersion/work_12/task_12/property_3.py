'''
Setter
- метод, контрролирующий изменение свойства

class Name:
    ...
        @property
        def param(self):
            ...
            return ...

        @param.setter
        def param(self, value):
            ...
            self._param = value
 
'''

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > self._age:
            self._age = value
        else:
            raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')

user = User('Стивен', 'Спилберг')
user.age = 75
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошёл один год.')
user.age = 76
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошло несколько лет. Изобретена технология омоложения. Но возраст она не уменьшает.')
user.age = 25   # ValueError: Новый возраст должен быть больше текущего: 76


# Создаем свойство age, для чтения текущего возраста
# Создаем сеттер для age, для изменения возраста:
#     если возраст увеличивается, то значение меняется на новое
#     возраст не может уменьшится, поэтому будет ошибка
# Имя сеттера должно быть такое же как и у свойства
# Логика в сеттере можебыть любая и не обязательно вызывать ошибки
