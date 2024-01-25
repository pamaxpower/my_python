"""
Разработка через тестирование TDD

TDD - test_driven development
- техника разработки ПО, которая основывается на повторении 
очень коротких циклов разработки: сначала пишется тест, 
покрывающий желаемое изменение, потом пишется код, 
который позволяет пройти этот тест, а затем проводится 
рефакторинг кода к соответствующим стандартам

Этапы TDD:
* добавление теста
* запуск все тестов (чтобы убедиться, что новые тесты не проходят)
* Написание кода
* Запуск всех тестов (чтобы убедиться, что все тесты проходят)
* Рефакторинг
"""

# Добавим в нашу функцию новые тесты:
# * проверка на натуральное число:
#     * если целое -> ошибка типа
#     * если целое, но не натуральное -> ошибка значения
# * тест для единицы
# * тест на большие числа (составные и простые) -> 
# будет предупреждение о долгом поиске (если число больше 100 млн)

def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time.
    Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time.
    Working...
    True
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
