import telebot
from telebot import types

bot = telebot.TeleBot('7508498759:AAFlBnKsQ8CTlwn2zjXT8xp_b83wgXHUodc')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("глянуть ссылки")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "автор идеи ждет автобус и мутит темки на несколько лямов, но ссылки вот", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'глянуть ссылки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton("ссылка 1")
        btn2 = types.KeyboardButton("ссылка 2")
        markup.add(btn1, btn2,)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть