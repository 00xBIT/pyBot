import telebot
from telebot import types

class TeleManager():

	def func(self):
		bot = telebot.TeleBot("MY_TOKEN")

		@bot.message_handler(func=lambda message: True)
		def echo_message(message):
			bot.reply_to(message, message.text)

		bot.polling(none_stop=True, interval=0, timeout=10)
