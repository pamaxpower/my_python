'''
Обработка ошибок ввода с помощью цикла while True

- применяется в случае, когда пользователь будет бесконечно вводить данные, 
пока не будет нужного результата

'''

def get(text: str = None) -> int:
    while True:
        try:
            num = int(input(text))
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'f'Попробуйте снова')
    return num

if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')

# бесконечный цикл while True прерывается командой break
# если пользователь введет целое число, код отработает без ошибок и программа выйдет из цикла цршду