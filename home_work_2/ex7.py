'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11
'''


num = float(input())
sum = 0
if num >=1:
    while num != 0:
        digit = num % 10
        sum += digit
        num = num // 10
else:

print(sum)