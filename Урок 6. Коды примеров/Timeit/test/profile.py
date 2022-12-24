from timeit import timeit
from code import concat_test

print(timeit("concat_test()", globals=globals(), number=1000))

# print(timeit("concat_test()", setup="from code import concat_test",
# number=1000))
