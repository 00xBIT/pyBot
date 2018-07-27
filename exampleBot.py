import telebot
import logging
from telebot import types
API_TOKEN = 'my token'
 
bot = telebot.TeleBot(API_TOKEN)
#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG)
 
helloMessage = """\
Привет!
"""
 
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, helloMessage)
 
 
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)   
    
 
bot.polling(none_stop=True, interval=0, timeout=3)

