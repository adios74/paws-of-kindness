import telebot
from telebot import types
import get_data
import information
import donation_info
import time


bot = telebot.TeleBot('7063861683:AAEj42JKRsa2Qst1aigI9VyK4wX3EfzFfG8')
# 7063861683:AAEj42JKRsa2Qst1aigI9VyK4wX3EfzFfG8

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Собаки', callback_data='dogs')
    button2 = types.InlineKeyboardButton('Кошки', callback_data='cats')
    markup.row(button1, button2)
    button3 = types.InlineKeyboardButton('Пожертвования', callback_data='donate')
    button4 = types.InlineKeyboardButton('Полезная информация', callback_data='info')
    markup.row(button3, button4)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Чем мы можем вам помочь?', reply_markup = markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global get_pet, get_name, i
    if callback.data == 'dogs':
        i = 0
        markup = types.InlineKeyboardMarkup()
        dogbutton1 = types.InlineKeyboardButton('◀️', callback_data='prev')
        dogbutton2 = types.InlineKeyboardButton('▶️', callback_data='next')
        dogbutton3 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(dogbutton1, dogbutton2)
        markup.row(dogbutton3)
        get_name = get_data.get_dogs_name
        get_pet = get_data.get_dog
        name, i = get_name(i,0)
        path, description = get_pet(name)
        file = open(path, 'rb')
        bot.send_photo(callback.message.chat.id, file, description, reply_markup=markup)
    if callback.data == 'next':
        markup = types.InlineKeyboardMarkup()
        petbutton1 = types.InlineKeyboardButton('◀️', callback_data='prev')
        petbutton2 = types.InlineKeyboardButton('▶️', callback_data='next')
        petbutton3 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(petbutton1, petbutton2)
        markup.row(petbutton3)
        name, i = get_name(i,1)
        path, description = get_pet(name)
        file2 = open(path, 'rb')
        photo = types.InputMediaPhoto(file2)
        bot.edit_message_media(chat_id=callback.message.chat.id, message_id=callback.message.message_id, media=photo)
        bot.edit_message_caption(description, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == 'prev':
        markup = types.InlineKeyboardMarkup()
        petbutton1 = types.InlineKeyboardButton('◀️', callback_data='prev')
        petbutton2 = types.InlineKeyboardButton('▶️', callback_data='next')
        petbutton3 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(petbutton1, petbutton2)
        markup.row(petbutton3)
        name, i = get_name(i, -1)
        path, description = get_pet(name)
        file2 = open(path, 'rb')
        photo = types.InputMediaPhoto(file2)
        bot.edit_message_media(chat_id=callback.message.chat.id, message_id=callback.message.message_id, media=photo)
        bot.edit_message_caption(description, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == 'cats':
        i = 0
        markup = types.InlineKeyboardMarkup()
        catbutton1 = types.InlineKeyboardButton('◀️', callback_data='prev')
        catbutton2 = types.InlineKeyboardButton('▶️', callback_data='next')
        catbutton3 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(catbutton1,catbutton2)
        markup.row(catbutton3)
        get_name = get_data.get_cats_name
        get_pet = get_data.get_cat
        name, i = get_name(i, 0)
        path, description = get_pet(name)
        file = open(path, 'rb')
        bot.send_photo(callback.message.chat.id, file, description, reply_markup=markup)
    if callback.data == 'donate':
        markup = types.InlineKeyboardMarkup()
        donationbutton = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(donationbutton)
        bot.send_message(callback.message.chat.id, donation_info.donation_text, reply_markup=markup)
    if callback.data == 'info':
        markup = types.InlineKeyboardMarkup()
        info_button1 = types.InlineKeyboardButton('породах собак', callback_data='dogs_info')
        info_button2 = types.InlineKeyboardButton('породах кошек', callback_data='cats_info')
        info_button3 = types.InlineKeyboardButton('первых днях в новом доме', callback_data='new_home_info')
        markup.row(info_button1, info_button2)
        markup.row(info_button3)
        bot.send_message(callback.message.chat.id, 'Информация о...', reply_markup=markup)
    if callback.data == 'new_home_info':
        markup = types.InlineKeyboardMarkup()
        new_home_info_button1 = types.InlineKeyboardButton('🐶', callback_data='new_home_info_dog')
        new_home_info_button2 = types.InlineKeyboardButton('🐱', callback_data='new_home_info_cat')
        new_home_info_button3 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(new_home_info_button1, new_home_info_button2)
        markup.row(new_home_info_button3)
        bot.send_message(callback.message.chat.id, 'Информация о первых днях животного в новом доме', reply_markup=markup)
    if callback.data == 'new_home_info_dog':
        markup = types.InlineKeyboardMarkup()
        new_home_info_dog_button = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(new_home_info_dog_button)
        bot.send_message(callback.message.chat.id, information.first_days_info_dog, reply_markup=markup)
    if callback.data == 'new_home_info_cat':
        markup = types.InlineKeyboardMarkup()
        new_home_info_cat_button = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(new_home_info_cat_button)
        bot.send_message(callback.message.chat.id, information.first_days_info_cat, reply_markup=markup)
    if callback.data == 'dogs_info':
        markup = types.InlineKeyboardMarkup()
        dogsinfo1button1 = types.InlineKeyboardButton('🏠', callback_data='home')
        dogsinfo1button2 = types.InlineKeyboardButton('▶️', callback_data='nextdoginfo')
        markup.row(dogsinfo1button2)
        markup.row(dogsinfo1button1)
        bot.edit_message_text(information.dogs_text1, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == 'nextdoginfo':
        markup = types.InlineKeyboardMarkup()
        dogsinfo2button1 = types.InlineKeyboardButton('🏠', callback_data='home')
        dogsinfo2button2 = types.InlineKeyboardButton('◀️', callback_data='dogs_info')
        markup.row(dogsinfo2button2)
        markup.row(dogsinfo2button1)
        bot.edit_message_text(information.dogs_text2, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == 'cats_info':
        markup = types.InlineKeyboardMarkup()
        catsinfobutton1 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(catsinfobutton1)
        bot.edit_message_text(information.cats_text, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == 'home':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Собаки', callback_data='dogs')
        button2 = types.InlineKeyboardButton('Кошки', callback_data='cats')
        markup.row(button1, button2)
        button3 = types.InlineKeyboardButton('Пожертвование', callback_data='donate')
        button4 = types.InlineKeyboardButton('Полезная информация', callback_data='info')
        markup.row(button3, button4)
        bot.send_message(callback.message.chat.id, f'Чем мы можем вам помочь?', reply_markup=markup)
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет' or message.text.lower() == 'здравствуйте':
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Введите /start, чтобы начать.', parse_mode='html')
    elif message.text.lower() == 'помощь' or message.text.lower() == 'помогите' or message.text.lower() == 'помоги':
        bot.send_message(message.chat.id, f'Введите /start, чтобы начать', parse_mode='html')

i = 0
get_pet = ''
get_name = ''
# bot.polling(non_stop=True)
if __name__=='__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue