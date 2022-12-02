'''a = int(input())
b = int(input())
sum = 0
max_del = 0
for i in range(a,b+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += j
        if count >= sum and i >= max_del:
            sum = count
            max_del = i

print(max_del, sum)'''

'''import math

num = int(input())
sum = 0
for i in range(1, num+1):
    sum += math.factorial(i)
print(sum)'''

a = int(input())
b = int(input())

for i in range(a, b+1):
    # flag = True
    for j in range(2, i):
        print(i, j)
        if i % j == 0:
            continue