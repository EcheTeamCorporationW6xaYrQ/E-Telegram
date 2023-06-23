import telebot 
from telebot import types
from init.py import bot 

banned_id = [] #для реалізації банів
user_content = {}
commented = False

@bot.message_handler(commands=['start']) #на команду старт
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привітатися")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привіт! Я - бот EChernihiv!", reply_markup=markup)

@bot.message_handler(chat_types=['private'], commands=['content']) #на команду контент
def content(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_content[user_id] = {'text': None, 'media': None}
    bot.send_message(chat_id=chat_id, text="Напишіть новину, яку ви хочете запропонувати.")
    bot.register_next_step_handler(message, process_content_text)
    
def process_content_text(message): #обробляє текст контенту
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.chat.username
    admin_id = #ТРЕБА ПОСТАВИТИ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    user_content[user_id]['text'] = message.text
    
    keyboard = types.InlineKeyboardMarkup()
    approve_button = types.InlineKeyboardButton(text="Схвалено", callback_data=f"approve {user_id}")
    reject_button = types.InlineKeyboardButton(text="Відхилено", callback_data=f"reject {user_id}")
    comment_button = types.InlineKeyboardButton(text="Прокоментувати", callback_data=f"comment {user_id}")
    keyboard.add(approve_button, reject_button, comment_button)
    bot.send_message(chat_id=admin_id, text=f"Користувач @{username} надіслав наступний контент: {message.text}", reply_markup=keyboard)
    bot.send_message(chat_id=chat_id, text="Надішліть фото/відео контент (не обов'язково, якщо не збираєтеся напишіть: ні)")

    user_content[user_id]['media'] = None

    bot.register_next_step_handler(message, process_content_media)

def process_content_media(message): # опрацьовує медіа контент
    try:
       user_id = message.from_user.id
       chat_id = message.chat.id
       username = message.chat.username
       if message.content_type == 'photo':
             user_content[user_id]['media'] = message.photo[-1].file_id
       elif message.content_type == 'video':
             user_content[user_id]['media'] = message.video.file_id
       else:
             user_content[user_id]['media'] = None

       if user_content[user_id]['media']:
              if message.content_type == 'photo':
                      bot.send_message(chat_id=admin_id, text=f"Користувач @{username} надіслав фото:")
                      bot.send_photo(chat_id=admin_id, photo=user_content[user_id]['media'])
              elif message.content_type == 'video':
                      bot.send_message(chat_id=admin_id, text=f"Користувач @{username} надіслав відео:")
                      bot.send_video(chat_id=admin_id, video=user_content[user_id]['media'])
       else:
            bot.send_message(chat_id=admin_id, text=f"Користувач @{username} не надіслав медіа контент.")
            bot.send_message(chat_id=admin_id, text=message.text)
    except Exception as e:
          print(e)
            
# опрацьовує натиснення на кнопки схвалити/відхилити/прокоментувати
@bot.callback_query_handler(lambda call: call.data.startswith(('approve', 'reject', 'comment')))
def process_callback(call):
    user_id = int(call.data.split()[1])
    admin_id = #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if call.data.startswith('comment'):
        commented = True
        bot.send_message(chat_id=admin_id, text=f"Надішліть ваш коментар користувачу {user_id}.")
    else:
        if call.data.startswith('approve'):
            bot.send_message(chat_id=user_id, text="Ваш контент схвалений. Дякую за співпрацю.")
        elif call.data.startswith('reject'):
            bot.send_message(chat_id=user_id, text="Вибачте, але Ваш контент відхилений.")

        del user_content[user_id]  # Чистимо словник після
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        if user_id in user_content:
            user_content.pop(user_id)
        else:
            pass
            
#мені довелося їбанути жоский костиль тут, тому прочитати оце обов'язково!!
#аби надіслати коментар користувачу необхідно використати таку форму:
#<id> comment
#через пробіл, інакше програма піде по пизді

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if commented:
      commented=False                                            #реалізація механізму
      user_id = int(message.text.split()[0])
      msg_content = message.text.split()[1]
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("На головну")
      markup.add(btn1)
        
      bot.send_message(chat_id=user_id, text=msg_content, reply_markup=markup)
      del user_content[user_id]
      bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
      #чистка
      if user_id in user_content:
          user_content.pop(user_id)
      else:
          pass
      
    elif message.text == "👋 Привітатися" or message.text == "На головну":
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
        
    elif message.text == "Запропонувати новину":
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("На головну")
      markup.add(btn1)
      bot.send_message(message.from_user.id, "Для того, щоб запропонувати нам новину, скористайтеся командою /content", reply_markup=markup)

    
        
@bot.message_handler(commands=['status']) #допилити
def get_text_messages(message):
