from random import randint as rd
from time import sleep as sl

dict_res = {}

def result_game(question, num):
    dict_res[question] = num
    return dict_res



def riddle_game(text, variants, attempt):
    
    print(f'Вот моя загадка: {text}')
    sl(3)
    print(f'У тебя есть {attempt} попытки')
    sl(1)
    count = 1
    while count <= attempt:

        user_answer = input('Что это? Ваш ответ: ').lower()
        if user_answer in variants:
            print(f'Молодец! Ты угадал с {count} попытки')
            flag = count
            break
        else:
            count += 1
            print('Неправильно!')

  
        if count > attempt:
            print('Попытки закончились! ТЫ проиграл!')
            flag = 0

    result_game(text, flag)
    return flag

def change_riddle():
    print('Приветствую. тебя в моей игре!')
    sl(1)
    print('Правила простые: Я задаю загадку, а ты ее угадываешь')
    sl(3)
   
    my_dict = {
        'Висит груша - нельзя скушать': ["лампа", "лампочка", "люстра"],
        'Зимой и летом одним цветом': ["елка", "ёлка", "ель"]
        # 'Кто его раздевает, тот слезы проливает': ["лук", "лучок", "луковица"],
        # 'На грядочке зеленые, а в баночке соленые': ["огурец", "огурцы"],
        # 'Конь стальной, хвост льняной': ["игла с ниткой", "иголка и нитка", "иголка"],
        # 'Два брюшка, четыре ушка': ["подушка"],
        # 'Туда-сюда-обратно, о, боже, как приятно': ["качели"]
        }
    for key, values in my_dict.items():
        riddle_game(key, values, rd(1,3))
        print()
        sl(3)




    



