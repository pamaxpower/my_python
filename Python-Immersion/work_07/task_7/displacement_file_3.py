'''
Методы перемещения в файле

truncate(size=None) - метод изменяет размер файла
- если не передать значение size, то все что после текущего положения курсора обрежется
- если указать size, то все от начала файла до size оставляем, остальное удаляется
'''

last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))
    print(f.truncate())

# хочу обрезать файл по значению 64

# size = 64
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     print(f.truncate(size))
