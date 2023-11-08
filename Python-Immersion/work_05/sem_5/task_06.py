'''
Задание №6
✔ Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку.
'''

print(*(f'\n' if j==11 else f'{j} x {i} = {i*j}'.ljust(11) for i in range(2, 10) for j in range(2, 12)))
