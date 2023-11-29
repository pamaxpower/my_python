'''
Задание №5

Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов
'''
from os import listdir
from json import load
import pickle 

def func(directory_name):
    for el in listdir(directory_name):
        if el.endswith('.json'):
            with open (el, 'r', encoding='utf-8') as f:
                res = load(f)

            path = ''.join(el.split('.')[:-1]) + '.pickle'
            with open (path, 'wb') as pickle_file:
                pickle.dump(res, pickle_file)
         


func('C:/Users/Lenovo/MyPython/Python-Immersion/work_08/sem_8')