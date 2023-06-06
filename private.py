import telebot 
from telebot import types
from init.py import bot 

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if update.message.chat_id == {}:           #наш чат айді, треба змінити!! необхідне для керування в цілях безпеки
     if message.text == "/status": 
        #має виводити статус сайту
        
