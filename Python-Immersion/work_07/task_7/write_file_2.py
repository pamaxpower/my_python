'''
Запись и добавление в файл

w - создаем пустой файл для записи, 
если файл уже есть, то открывается файл, и удаляются все записи в нем

x - создаем пустой файл, если файл существует, вызывем ошибку

a - открываем существующий файл для записи данных в конец
если файла не существует, создаем новый файл

f.writelines('\n'.join(text)) - запись методом writelines()
- не возвращает кол-во записанной информации
- записывает одну большую строчку но символы переноса не добавляет

'''

text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 
         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?', 
         'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]

with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))
