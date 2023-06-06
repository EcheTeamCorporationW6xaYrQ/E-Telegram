import telebot 
from telebot import types
from init.py import bot 

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  
