'''
Функция генератор. Ключевое слово yield

- ключевое слово yield работает как return

'''

# обычная функция

def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result

# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')



def factorial_2(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

for i, num in enumerate(factorial_2(10), start=1):
    print(f'{i}! = {num}')
