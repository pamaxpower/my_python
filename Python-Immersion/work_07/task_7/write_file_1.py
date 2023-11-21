'''
Запись и добавление в файл

w - создаем пустой файл для записи, 
если файл уже есть, то открывается файл, и удаляются все записи в нем

x - создаем пустой файл, если файл существует, вызывем ошибку

a - открываем существующий файл для записи данных в конец
если файла не существует, создаем новый файл

res = f.write(text) - запиь методом write()

- после записи метод возвращает кол-во записанной информации
- вся информация записывается в одну строку.
Дело в том, что метод write() не добавляет символ переноса строки.
для записи строки с переносом, нужно добавить символ '\n'

'''

# text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
# with open('new_data.txt', 'a', encoding='utf-8') as f:
#     res = f.write(text)
#     print(f'{res = }\n{len(text) = }') 

text1 = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 
         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?', 
         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]

with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text1:
        # res = f.write(line)       # запись без переноса строки
        res = f.write(f'{line}\n')  # запись строки с переносом
        print(f'{res = }\n{len(line) = }')

# вся информация записывается в одну строку. Дело в том, 
# что метод write() не добавляет символ переноса строки
# для записи строки с переносом, нужно добавить символ записи в метод write()
