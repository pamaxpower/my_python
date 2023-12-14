'''
На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать 
числа из вашего билета из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.


Пример входных данных:

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

Пример выходных данных:

Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7
'''

class LotteryGame():
    def __init__(self, ticket, result):
        self._ticket = ticket
        self._result = result

    
    def compare_lists(self):
        count = 0
        res = []
        for el1 in self._ticket:
            for el2 in self._result:
                if el1==el2:
                    count += 1
                    res.append(el1)
                    break

        if count == 0:
            return print(f'Совпадающих чисел нет.')
        else:
            return print(f'Совпадающие числа: {res}\nКоличество совпадающих чисел: {count}')
        

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

# list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()