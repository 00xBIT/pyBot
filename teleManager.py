import telebot
import logging
from telebot import types
 
 
class teleManager:
    __API_TOKEN = ''
    __helloMessage = """\
        Привет!
        """
    __bot = None
 
    def __init__(self, token):
        self.__API_TOKEN = token
 
        self.__bot = telebot.TeleBot(self.__API_TOKEN)
        #logger = telebot.logger
        #telebot.logger.setLevel(logging.DEBUG)
 
    def run(self):
        print('start')
 
        @self.__bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            bot.reply_to(message, helloMessage)
 
        self.__bot.polling(none_stop=True, interval=0, timeout=3)
