from timeit import timeit
from memory_profiler import profile

x = 123

@profile
def sum_digit(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total

@profile
def print_digit_sum(a):
    lst = {int(i) for i in str(a)}
    sum(lst)


sum_digit(x)
#print(f'1 способ: {timeit("sum_digit(x)",  globals=globals(), number=100000)}')
# 1 способ: 0.203022400382906


print_digit_sum(x)
#print(f'2 способ: {timeit("print_digit_sum(x)",  globals=globals(), number=100000)}')
# 2 способ: 0.23104560002684593

