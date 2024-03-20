import telebot
from random import *
import json
import requests


films = []
API_URL = 'https://7012.deeppavlov.ai/model'

def load():
    global films
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека была успешно загружена") 


API_TOKEN = '6717423415:AAEbuQmIZm5yY3j3iGBBESNl2m0T0ier5fs'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id, "Фильмотека была успешно загружена!")

    except Exception:
        films.append("Матрица")
        films.append("Солярис")
        films.append("Властелин колец")
        films.append("Техасская резня бензопилой")
        films.append("Санта Барбара")
        bot.send_message(
            message.chat.id, "Фильмотека была загружена по умолчанию!")


@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id, "Вот список фильмов")
        bot.send_message(message.chat.id, ", ".join(films))
    except Exception:
        bot.send_message(message.chat.id, "Список фильмов пуст")


@bot.message_handler(commands=['save'])
def save_all(message):
    with open("films.json", "w+", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    bot.send_message(message.chat.id, "Наша фильмотека была успешно сохранена в файле films.json")


@bot.message_handler(commands=['add'])
def add_film(message):
    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, "Укажите название фильма")
    else:
        film_name = " ".join(message.text.split()[1:])
        films.append(film_name)
        bot.send_message(message.chat.id, "Фильм добавлен!")


@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]    # на выходе список из сообщения, кроме команды
    
    qq = " ".join(quest)                # преобразования списка в строку
    
    # подготавливаем словарь, где ключ 'question_raw', а значение - наш текст
    data = {'question_raw': [qq]}       
    try:
        # Выполняем запрос методом post (куда, что отправляем)
        res = requests.post(API_URL, json=data, verify=False).json()
        # res - результат запроса
        bot.send_message(message.chat.id, res)
    except Exception:
        bot.send_message(message.chat.id, "Что-то я ничего не нашел :-(")


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if 'привет' in message.text.lower():
        bot.send_message(message.chat.id, "Hello")

    if 'дела' in message.text.lower():
        bot.send_message(message.chat.id, "Дела хорошо. Сам как?")

bot.polling()