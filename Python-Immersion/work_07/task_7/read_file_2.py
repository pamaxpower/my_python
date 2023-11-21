'''
Чтение файла

2) res = f.read() - считывает файл целиком (если () или (n=-1)) 
или порциями (если (n)) по n-символов или n-байт информации из файла

если файл уже прочтен, то повторный вызов метода вернет пустую строку
'''
# читаем весь файл

with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')


# читаем по 20 символов, а не весь файл

# SIZE = 20
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.read(SIZE):
#         print(res)
