'''
Напишите небольшую программу, которая запрашивает у пользователя любой текст
и выводит о нём следующую информацию:
✔ тип объекта,
✔ адрес объекта в оперативной памяти,
✔ хеш объекта.
'''

txt = input('Введите ваш текст: ')
print(f'Тип объекта: {type(txt)}')
print(f'Адрес объекта: {id(txt)}')
print(f'Хэш объекта: {hash(txt)}')
