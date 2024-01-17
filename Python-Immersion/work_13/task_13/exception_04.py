'''
Команда except
- идет после блока try и отвечает за обработку исключений

try:
    # место кода, где возможна ошибка
except NameError as e:
    # действие кода при ошибки NameError
# продолжаем работу кода

переменная e сохраняет информацию об ошибке
'''

def get(text: str = None) -> int:
    data = input(text)
    try:
        num = int(data)
    except ValueError as e:
        print(f'Ваш ввод привёл к ошибке ValueError: {e}')
        num = 1
        print(f'Будем считать результатом ввода число {num}')
    return num

if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')
