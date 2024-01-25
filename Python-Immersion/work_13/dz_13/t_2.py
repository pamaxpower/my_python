"""
Допишите в вашу задачу Archive обработку исключений.

Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст не является строкой или является пустой строкой.

Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'

И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом с плавающей запятой.

Текст ошибки: 'Invalid number: {введенное число}. Number should be a positive integer or float.'


"""



from typing import Union

class InvalidTextError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Invalid text: {self.text}. Text should be a non-empty string.'

class InvalidNumberError(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Invalid number: {self.number}. Number should be a positive integer or float.'

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or text == '':
            raise InvalidTextError(text)
        if not isinstance(number, (int, float)) or number <= 0:
            raise InvalidNumberError(number)
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self._instance.archive_text} and {self._instance.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'
    
invalid_archive_instance = Archive("1", 5)
print(invalid_archive_instance)


