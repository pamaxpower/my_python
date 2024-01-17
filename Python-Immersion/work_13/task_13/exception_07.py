'''
Несколько except для одного try
'''

def hundred_div_num(text: str = None) -> tuple[int, float]:
    while True:
        try:
            num = int(input(text))
            div = 100 / num
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                  f'Попробуйте снова')
        except ZeroDivisionError:
            div = float('inf')
            # float(‘inf’) - бесконечность
            # float(‘-inf’) - минус бесконечность
            break
    return num, div


if __name__ == '__main__':
    n, d = hundred_div_num('Введите целый делитель: ')
    print(f'Результат операции: "100 / {n} = {d}"')
