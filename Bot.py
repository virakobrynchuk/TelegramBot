#!/usr/bin/env python
import random

import telebot
from telebot.types import Message

TOKEN = '723397720:AAHOQdCN7xTJW81850S_0n_1lWz3mi2UhYc'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'There is no answer =(')


@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'Привет' in message.text:
        bot.reply_to(message, 'Привет Вера')
        return
    bot.reply_to(message, str(random.random()))


bot.polling(timeout=60)
