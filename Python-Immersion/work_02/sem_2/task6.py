'''
Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, 
но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия 
начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, 
вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

start_sum = 0
count_add = 0
count_out = 0

while True:
    if start_sum > 5_000_000:
        start_sum -= start_sum * 0.1
        print(f'С вас сняли налог на роскошь в размере {start_sum * 0.1} рублей')
    
    action = input('Введите команду: ')

    if action == 'q':
        print(f'Ваш баланс: {start_sum}')
        print('Выход из банкомата')
        break
    elif action == 'a':
        sum_add = int(input('Введите сумму: '))
        if sum_add % 50 == 0:
            start_sum += sum_add
            count_add += 1
            if count_add % 3 == 0:
                start_sum *= 1.03
        else:
            print('Введена некоректная сумма: ')
    elif action == 'o':
        sum_out = int(input('Введите сумму: '))
        comission = sum_out * 0.015
        if comission < 30:
            commission = 30
        elif comission > 600:
            commission = 600
        if sum_out + comission > start_sum:
            print('Средств недостаточно: ')
        else:
            if sum_out % 50 == 0:
                start_sum -= (sum_out + comission)
                count_out += 1
                if count_out % 3 == 0:
                    start_sum *= 1.03
            else:
                print('Введена некоректная сумма: ')
    print(f'Ваш баланс: {start_sum}')
