try:
    print(100/0)
except:
    print("Деление на ноль недопустимо")

# Деление на ноль недопустимо

try:
    res = 100/0
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(f"Все хорошо. Результат - {res}")
finally:
    print("Программа завершена")

"""
Деление на ноль недопустимо
На ноль делить нельзя
Программа завершена
"""
