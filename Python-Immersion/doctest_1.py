"""
doctest - тестирование документации
- проверка актуальности строк документации путем 
проверки того, что все интерактивные примеры работают в соответствии с документацией
- для регрессионного тестирования - убедиться, что 
все интерактивные примеры из тестового файла или объекта работают 
должным образом
- позволяют написать учебную документацию для пакета: 
примеры и пояснительный текст ("грамотное тестирование" 
или "исполняемая документация")
"""

def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

help(is_prime)