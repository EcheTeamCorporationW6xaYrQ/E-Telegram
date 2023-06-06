import telebot
from telebot import types

bot = telebot.TeleBot('6204641970:AAGrEMOsXkZygElfxbQlQzP5QknVAeU66VY')

@bot.message_handler(commands=['start']) 
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_site = types.KeyboardButton('Наш сайт')               #приклад ініціалізації кнопок
  markup.add(button_site)             
  bot.send_message(message.from_user.id, "Вітаю! Я - бот ЄЧернігова!", reply_markup=markup) #відповідь на /start
  
@bot.message_handler(content_types=['text'])                   #відповіді бота
def get_text_messages(message):
  if message.text == "Наш сайт": 
    bot.send_message(message.from_user.id, "На жаль, наразі цей ресурс недоступний", reply_markup=markup)
    
bot.polling(none_stop=True, interval=0)                         #необхідна частина щоб бот постійно працював
