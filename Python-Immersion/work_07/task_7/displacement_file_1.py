'''
Методы перемещения в файле

f.tell() - возвращает текущую позицию в файле

'''

text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?', 
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]

with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())     # каждый раз после записи смотрим где находится курсор
    print(f.tell())         # после завершения цикла записи, курсор также находится в конце файла

print(f.tell())     # ValueError: I/O operation on closed file.
# после закрытия файла мы не может определить позицию курсора