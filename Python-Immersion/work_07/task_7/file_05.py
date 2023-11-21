'''
Менеджер контекста with open()

with гарантирует закрытие файла и сохранение информации
'''

with open('text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
print(f.write('Пока'))  # ValueError: I/O operation on closed

# 3 строка кода выдаст ошибку, потому что переменная f была 
# определена в менеджере контекста, а он закрылся на 2 строке 