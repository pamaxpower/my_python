'''
Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
Пример: Для N = 5: 1, -3, 9, -27, 81
'''

n = int(input())
result = []
for i in range(n):
    if i % 2 == 0:
        print((-3)**i, end=' ')
    else:
        print((-3)**i, end=' ')
    result.append(str((-3)**i))
print()   
print(', '.join(result), end='')