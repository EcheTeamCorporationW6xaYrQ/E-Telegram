import telebot 
from telebot import types
from init.py import bot 

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привітатися")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привіт! Я - бот EChernihiv!", reply_markup=markup)

@bot.message_handler(chat_types=['private']) # You can add more chat types
def command_help(message):
    bot.send_message(message.chat.id, 'Private chat detected, sir!')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  
    if message.text == "👋 Привітатися" or message.text == "На головну":
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Запропонувати новину") #треба додати смайликів
      btn2 = types.KeyboardButton("Про EChernihiv")
      btn3 = types.KeyboardButton("Наш сайт")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.from_user.id, "Чим можу служити Вам?", reply_markup=markup)
                       
    elif message.text == "Про EChernihiv":
      markup = types.ReplyKeyboardMarkup(resize_keyobard=True)
      btn1 = types.KeyboardButton("На головну")
      markup.add(btn1)
      bot.send_message(message.from_user.id, "ECHERNIHIV IS A VERY COOL TEMA REALLY!!!!", reply_markup=markup) #ЗМІНИТИ!!!!!
      
    elif message.text == "Наш сайт":
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("На головну")
      markup.add(btn1)
      bot.send_message(message.from_user.id, "INFO ABOUT SITE AND A LINK", reply_markup=markup) #ЗМІНИТИ!!!
      
@bot.message_handler(commands=['status'])
def get_text_messages(message):
                     
        
        
