'''
Команда finally
- срабатывает во всех случаях: если ошибка была, и если ее не было
try:
    # отлавливает ошибку
except NameError as e:
    # действие при ошибке NameError
finally:
    # выполняется в любом случае


'''

def get(text: str = None) -> int:
    num = None
    try:
        num = int(input(text))
    except ValueError as e1:
        print(f'Ваш ввод привёл к ошибке ValueError: {e1}')
    finally:
        return num if isinstance(num, int) else 1

if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    try:
        print(f'100 / {number} = {100 / number}')
    except ZeroDivisionError as e2:
        print(f'На ноль делить нельзя. Получим {e2}')