'''
Логические типы

bool(x) — возвращает логическое значение,
т.е. одно из двух: True или False.

'''

DEFAULT = 42
num = int(input('Введите уровень или ноль для значения по умолчанию: '))

# конструкция ленивый if: если True, то вернет введениое значение, если False, то вернет значение по умолчанию
level = num or DEFAULT

print(level)


name = input('Как вас зовут? ')
# если введенная строка пустая, то вернется "привет, аноним"
if name:
    print(f'Привет, {name}')
else:
    print('Привет, аноним')


data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# если список заполнен, цикл выполняется и вовзвращает последнее число списка, удаляя его из списка
# по мере того как список заканчивается и становится пустым, значение меняется с True на False и цикл прерывается
while data:
    print(data.pop()) 