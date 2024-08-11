import telebot
from telebot.types import Message
from time import sleep
from datetime import datetime
from keep_alive import keep_alive

keep_alive()

bot = telebot.TeleBot('2142995181:AAH7TXXCv4FU6n-_GqZ_7UCEga2p40GAFyg')

msgs:dict[int, bool] = {}

@bot.message_handler(commands=['start'])
def echo (msg: Message):
    
    global msgs
    
    id = msg.chat.id
    msgs[id] = True

    bot.reply_to(msg, 'running')
    
    c = 0
    while msgs[id]:
        c+=1
        t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        bot.send_message(id, f'{c} at {t}')
        sleep(60)

@bot.message_handler(commands=['stop'])
def echo (msg: Message):
    global msgs
    id = msg.chat.id
    msgs[id] = False

bot.infinity_polling()
