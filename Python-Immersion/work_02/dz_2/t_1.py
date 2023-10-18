'''
Напишите программу, которая получает целое число num и 
возвращает его шестнадцатеричное строковое представление.

Функцию hex используйте для проверки своего результата.
'''

num = int(input('Введите число: '))

def to_hex(number):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while number > 0:
        rem = number % 16
        result = hex_digits[rem] + result
        number //= 16
    return result

print(f"Шестнадцатеричное представление числа: {to_hex(num)}")
print(f'Проверка результата: {hex(num)}')