from timeit import timeit
from code1 import sum_max_elements
from code1 import sum_two_elements


n1, n2, n3 = int(input()), int(input()), int(input())
print(timeit("sum_max_elements(n1, n2, n3)", globals=globals(), number=1000))

# Время выполнения прграммы: 0.0003057001158595085э

print(timeit("sum_two_elements(num)", globals=globals(), number=1000))
