import telebot
import requests
bot = telebot.TeleBot("5797737730:AAGLdTGW6wiLIlM-EvYGOynNg6cu6-Tj_-A")
r=requests.get("https://api.cricapi.com/v1/currentMatches?apikey=831da77b-7b37-4ac2-b7c5-38209d127746&offset=0")

@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}! \nTo select any live match type this ->\n /selectmatch')
    # bot.send_message(message.chat.id, 'kkkk')

@bot.message_handler(commands=['selectmatch'])
def allMatches(message):
    print(message)
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!')
    

if __name__ == '__main__':
    bot.polling()
