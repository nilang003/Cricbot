import telebot
import requests
from app import cricFuntionality
bot = telebot.TeleBot("5797737730:AAGLdTGW6wiLIlM-EvYGOynNg6cu6-Tj_-A")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")



bot.polling()
