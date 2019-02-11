#!/usr/bin/env python
import random

import telebot
from telebot import types
from telebot.types import Message

TOKEN =
STICKER_ID =

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'There is no answer =(')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'Привет' in message.text:
        bot.reply_to(message, 'Привет Вера')
        return
    if 'Вакансия' in message.text:
        bot.reply_to(message, 'Хочешь узнать вакансии?')
        return
    if 'Да' in message.text:
        bot.reply_to(message, 'Javascript react developer, Разработчик смарт-контрактов')
        return
    bot.reply_to(message, str(random.random()))


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, STICKER_ID)
    # print(message)
    # print(message.sticker)


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


bot.polling(timeout=60)
