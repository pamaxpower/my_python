'''
Основы тестирования с pytest

Команда assert
- делает утверждение, если оно истино, то программа работает, 
если ложно - ошибка AssertionError

assert утверждение, "ложное утверждение"

Можно заменить конструкцией с if:

if утверждение:
    pass
else:
    raise AssertionError("Ложное утрверждение")

python -m pytest pytest_1.py -vv - для запуска с консоли
pytest pytest_1.py -vv (можно обращаться сразу к модулю)
'''

import pytest


def sum_two_num(a, b):
    # return a + b
    return f'{a}{b}'


def test_sum():
    assert sum_two_num(2, 3) == 5, 'Математика покинула чат'


if __name__ == '__main__':
    pytest.main()
