'''
Запись и добавление в файл

w - создаем пустой файл для записи, 
если файл уже есть, то открывается файл, и удаляются все записи в нем

x - создаем пустой файл, если файл существует, вызывем ошибку

a - открываем существующий файл для записи данных в конец
если файла не существует, создаем новый файл

print(text, file=f) - запись в файл функцией print()
- первая строка слиплась с последней строкой
'''
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 
         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?', 
         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]

with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        # print(line, file=f)
        print(line, end='***\n##', file=f)  #можно использовать для выделения записи


