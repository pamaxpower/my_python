'''num = int(input('Введите число: '))
mult = 1
while num > 10:
    mult *= num % 10
    num -= num % 10
print()'''

num = 7

print((num - num%10)//10)