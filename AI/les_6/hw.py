import telebot
from random import *
import json
import requests

API_URL = 'https://7012.deeppavlov.ai/model'
API_TRANSLATE = 'https://api-free.deepl.com/v2/translate'

API_TOKEN = '6717423415:AAEbuQmIZm5yY3j3iGBBESNl2m0T0ier5fs'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Готов к работе!")


@bot.message_handler(commands=['wiki'])
def wiki(message):
    # на выходе список из сообщения, кроме команды
    quest = message.text.split()[1:]

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


@bot.message_handler(commands=['translate'])
def translate(message):
    # Получаем текст для перевода, который идет после команды
    text = " ".join(message.text.split()[1:])

    # Подготавливаем данные для запроса
    # Перевод с русского на английский
    data = {'question_raw': [text], 'target': 'ru-en'}
    try:
        res = requests.post(API_TRANSLATE, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except Exception:
        bot.send_message(message.chat.id, "Что-то пошло не так :(")


@bot.message_handler(commands=['pogoda'])
def weather(message):
    city = message.text.split()[1]  # получаем название города из сообщения

    # URL для получения данных о погоде с accuweather.com
    # вместо YOUR_API_KEY вводим корректный API
    url = f"http://dataservice.accuweather.com/locations/v1/cities/search?q={city}&apikey=YOUR_API_KEY"
    
    try:
        response = requests.get(url).json()
        city_key = response[0]['Key']  # получаем ключ города
        weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{city_key}?apikey=YOUR_API_KEY"
        weather_info = requests.get(weather_url).json()
        # Получаем актуальную погоду для выбранного города
        weather_text = f"Сейчас в городе {city} {weather_info[0]['Temperature']['Metric']['Value']}°C, {weather_info[0]['WeatherText']}"

        bot.send_message(message.chat.id, weather_text)

    except Exception:
        bot.send_message(message.chat.id, "Что-то пошло не так. Попробуйте позже.")


bot.polling()
