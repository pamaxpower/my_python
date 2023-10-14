'''Напишите код, который анализирует число num и сообщает является ли оно 
простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело 
только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

'''

# while True:
#     num = int(input('Введите число: '))
#     if 0 < num <= 100000:
#         count = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         if count > 2:
#             print(f'{num} является составным числом')
#         else:
#             print(f'{num} является простым числом')
#         break
#     else:
#         continue



'''
num = int(input('Введите число: '))

res = f'Число {num} простое'
if not num % 2:
    res = f'Число {num} составное'
for dev in range(3, num // 2 + 1, 2):
    if not num % dev:
        res = f'Число {num} составное'
        break
print(res)
'''




def is_prime(num):
    if num < 2 or num > 100000:
        return "Число должно быть в диапазоне от 2 до 100000"
    
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return "Составное число"
    
    return "Простое число"

print(is_prime(int(input('Введите число: '))))


fghijMHqnopqrstuv xy01234=977 ;;7=3?fq 0=D>Eu
