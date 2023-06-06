import telebot
from telebot import types

bot = telebot.TeleBot('6204641970:AAGrEMOsXkZygElfxbQlQzP5QknVAeU66VY')
    
bot.polling(none_stop=True, interval=0)                         #необхідна частина щоб бот постійно працював
