'''
Представление для пользователя. 

дандер __str__ используется для получения удобного пользователю описания экземпляра

Общий вид:

class Person():
    ...

    def __str__(self):
        ...
        return 'Текст для пользователя'

'''

class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()
        
    def __str__(self):
        return f'Экземпляр класса User с именем "{self.name}"'

user = User('Спенглер')
print(user)
