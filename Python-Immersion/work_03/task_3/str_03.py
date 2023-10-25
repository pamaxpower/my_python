'''
Форматирование строк
'''

# через %
name = "Alex"
age = 12
text_1 = 'Меня зовут %s и мне %d лет' % (
    name, age)   # %s - строка, %d - числовой тип
print(text_1, '\n')

# через format()
text_2 = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text_2, '\n')

# с помощью f-строк
text_3 = f'Меня зовут {name} и мне {age} лет'
print(text_3)
