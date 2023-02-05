"""Модуль bytes"""

#text = 'Hello world!'
#text1 = b'Hello world!'

# строка в байтовом представлении
# форматы записи строки в байтах
BYTES_A = b'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'
BYTES_B = b"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430"
BYTES_C = b'''\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'''
print(BYTES_A)
print(type(BYTES_A))

# сстрока из символов относящихся к ASCII (латиница)
# всегда отображается как набор символов
BYTES_D = b'Program'
print(type(BYTES_D))
print(BYTES_D)

# строка из символов не относящихся к ASCII (кириллица)
# при попытке вывода байтового представления будет выведена ошибка
BYTES_E = b'Программа'
print(BYTES_E)
