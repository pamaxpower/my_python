'''
Строковые методы
'''

# .split() - разбивает строку на отдельные элементы

link = 'https://habr.com/ru/users/name1/posts/'
urls = link.split('/')
print(urls, '\n')

# a, b, c = input('Введите три числа через пробел: ').split()
# a, b, c, *_ = input('Введите не менее трех чисел черех пробел: ').split()
# print(c, b, a)

# .join() - склеивает строку
data = ['https:', '', 'habr.com', 'ru', 'users', 'name1', 'posts', '']
url = '/'.join(data)
print(url, '\n')

# Изменение регистра
text = 'однажды в СТУДЕНУЮ зИмнЮЮ ПоРУ'
print(text.upper())         # все буквы заглавные
print(text.lower())         # все буквы строчные
print(text.title())         # каждое слово с заглавной буквы
print(text.capitalize())    # предложение с заглавной буквы
print()

# .startswith(), .endswith() - проверка на совпадение с началом или концом строки
txt = 'Однажды в студеную зимнюю пору'
print(txt.startswith('Однажды'))
print(txt.endswith('зимнюю', 0, -5))
