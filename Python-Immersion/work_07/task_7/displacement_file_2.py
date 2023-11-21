'''
Методы перемещения в файле

seek(offset, whence=0) - принимает два аргумента

offset - смещение относительно опорной точки 
(положительное число - смещение вправо(вперед), 
отрицательное - смещение влево(назад))

whence - способ выбора опорной точки:
= 0 - отсчёт от начала файла (тогда offset - положительный)
= 1 - отсчёт от текущей позиции в файле
= 2 - отсчёт от конца файла (тогда offset - отрицательный)
(1 и 2) - ТОЛЬКО для чтения в двоичном режиме, исключение offset=0, тогда whence=2

'''
last = before = 0

text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?', 
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]

with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))
