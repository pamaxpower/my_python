'''
Поднятие исключений в классе
'''

class User:
    def __init__(self, name, age):
        if 6 < len(name) < 30:
            self.name = name
        else:
            raise ValueError(f'Длина имени должна быть между 6 и 30 символами. {len(name) = }')
        if not isinstance(age, (int, float)):
            raise TypeError(f'Возраст должен быть числом. Используйте int или float. {type(age) = }')
        elif age < 0:
            raise ValueError(f'Возраст должен быть положительным. {age = }')
        else:
            self.age = age

# user = User('Яков', '-12')  # ValueError: Длина имени должна быть между 6 и 30 символами. len(name) = 4
# user = User('Яковлев', '-12')  # TypeError: Возраст должен быть числом. Используйте int или float. type(age) = <class 'str'>
# user = User('Яковлев', -12)  # ValueError: Возраст должен быть положительным. age = -12
user = User('Яковлев', 12)  # все работает

