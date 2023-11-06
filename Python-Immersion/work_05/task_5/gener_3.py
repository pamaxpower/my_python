'''
Комбинации for / if в генераторах и выражениях

Классический код:

for expr in sequense1:
    if not condition1:
        continue
    for expr in sequense2:
        if not condition2:
            continue
        ...
        for expr in sequenseN:
            if not conditionN:
                continue

- каждый цикл вложен в предыдущий, 
логическая проверка определяет добавлять элемент в вывод 
или опустить его (continue)
                
Код-генератор:

gen = (expression for expr in sequense1 if condition1
        for expr in sequense2 if condition2
        for expr in sequense3 if condition3
        ...
        for expr in sequenseN if conditionN)

'''

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]

print(f'{len(x)=}\t{len(y)=}')

# mu = []
# for i in x:
#     if i % 2 != 0:
#         for j in y:
#             if j != 1:
#                 mu.append(i + j)
# print(len(mu), '\n', mu)

mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')
