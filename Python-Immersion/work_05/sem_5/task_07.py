'''
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''


def simple_num(n):
    count = 0
    num = 1
    is_simple = True
    while count < n:
        num += 1
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                is_simple = False
                break
            else:
                is_simple = True
        if is_simple:
            count += 1
            yield num


print(*simple_num(5))
