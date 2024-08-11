import telebot
from telebot.types import Message
from time import sleep
from datetime import datetime

bot = telebot.TeleBot('2142995181:AAH7TXXCv4FU6n-_GqZ_7UCEga2p40GAFyg')

@bot.message_handler(func=lambda _:True)
def echo(msg: Message):
    bot.reply_to(msg, 'running')
    c = 0
    while True:
        c+=1
        t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        bot.send_message(msg.chat.id, f'{c} at {t}')
        sleep(60)

bot.infinity_polling()
