import random
import telebot
from telebot import types

token = "5135599159:AAFvzsPk9y-gwYgkFMuJlDxyDZnZZLJ-2zU"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    keyboard.row("/кнб", "/анекдот", "/монетка")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?',
     reply_markup=keyboard)
    
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:')
    bot.send_message(message.chat.id, "1. Играть в камень, ножницы, бумага. Чтобы сыграть введите команду /кнб")
    bot.send_message(message.chat.id, "2. Выдавать анектоды. Для вызова анектода введите команду /анекдот")
    bot.send_message(message.chat.id, "3. Могу помочь сделать решение. Введите команду /монетка")

@bot.message_handler(commands=['кнб'])
def start_message(message):
    bot.send_message(message.chat.id, "Давайте сыграем. Играем честно, прописываем одновременно (введите один из атрибутов игры)")

@bot.message_handler(commands=['монетка'])
def start_message(message):
    a = random.randint(1,3)
    if a == 1: bot.send_message(message.chat.id, "Орел")
    if a == 2: bot.send_message(message.chat.id, "Решка")

@bot.message_handler(commands=['анекдот'])
def start_message(message):
    a = random.randint(1,4)
    if a == 1:  bot.send_message(message.chat.id, 'В Германии прошел чемпионат пива. Больше всех пива выпил житель Тамбова Гоша Сидоров, который смотрел чемпионат по телевизору')
    if a == 2:  bot.send_message(message.chat.id, "Слышу кто-то ходит в шкафу. Открываю - а там платья из моды выходят.")
    if a == 3:  bot.send_message(message.chat.id, "Когда в покере у меня на руках сильная комбинация я не подаю виду, потому что не знаю комбинаций.")
    


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
    if message.text.lower() == "ножницы":   bot.send_message(message.chat.id, "камень 🗿. Увы, вы проиграли")
    if message.text.lower() == "камень":  bot.send_message(message.chat.id, "бумага 📝. Увы, вы проиграли")
    if message.text.lower() == "бумага":  bot.send_message(message.chat.id, "Ножницы ✂. Увы, вы проиграли")

    
    if message.text.lower() == "xd": bot.send_message(message.chat.id, "xd = https://docs.google.com/document/d/1ORrShWqXm9PL9CZg9977SuMFsVJnZfz61kWOz9kYsuE/edit")
bot.infinity_polling()
