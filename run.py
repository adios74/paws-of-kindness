import telebot
import webbrowser
from telebot import types
import get_data
import pets_data.information as information
import donation_info
from init import bot_token
# from get_data import get_pet, get_name

bot = telebot.TeleBot(bot_token)


@bot.message_handler(command=['site', 'website'])
def site(message):
    webbrowser.open('https://vsemposobake.ru')

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

# @bot.message_handler(commands=['return_to_start'])
# def return_to_start(message):
#     markup = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton('Собаки', callback_data='dogs')
#     button2 = types.InlineKeyboardButton('Кошки', callback_data='cats')
#     markup.row(button1, button2)
#     button3 = types.InlineKeyboardButton('Пожертвование', callback_data='donate')
#     button4 = types.InlineKeyboardButton('Памятка владельцу собаки', url='https://vsemposobake.ru/wp-content/uploads/2018/07/Pamyatka_new.pdf')
#     markup.row(button3, button4)
#     button5 = types.InlineKeyboardButton('Полезная информация', callback_data='info')
#     markup.row(button5)
#     bot.send_message(message.chat.id, f'Чем мы можем вам помочь?', reply_markup = markup)

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
        # file = open('./собака Груша.jpg', 'rb')
        # bot.send_photo(callback.message.chat.id, file, 'Собака Груша\nГруше всего 8 месяцев.\nЭта очаровательная рыжая девчонка покоряет с первого взгляда- веселая, ласковая, невероятная оптимистка, ну как в такую не влюбиться ? Груша абсолютно открытый и доверчивый подросток, любит весь мир вокруг и верит, что впереди только радость. Очень любит обниматься, никогда не проявляет агрессии, нежная до невозможности, с радостью общается с другими собаками, так что готова стать и вторым питомцем в семье.', reply_markup = markup)
        get_name = get_data.get_dogs_name
        get_pet = get_data.get_dog
        name, i = get_name(i,0)
        path, description = get_pet(name)
        file = open(path, 'rb')
        bot.send_photo(callback.message.chat.id, file, description, reply_markup=markup)
    if callback.data == 'next':
        # file2 = open('./пёс Арчи.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        petbutton1 = types.InlineKeyboardButton('◀️', callback_data='prev')
        petbutton2 = types.InlineKeyboardButton('▶️', callback_data='next')
        petbutton3 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(petbutton1, petbutton2)
        markup.row(petbutton3)
        name, i = get_name(i,1)
        path, description = get_pet(name)
        # name, path, description = get_pet(get_name(1))
        file2 = open(path, 'rb')
        photo = types.InputMediaPhoto(file2)
        bot.edit_message_media(chat_id=callback.message.chat.id, message_id=callback.message.message_id, media=photo)
        # bot.send_photo(callback.message.chat.id, file2, description, reply_markup=markup)
        bot.edit_message_caption(description, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
        # bot.edit_message_media(callback.message.chat.id, callback.message.message_id, media=file2)
        # bot.edit_message_text(description, callback.message.chat.id, callback.message.message_id)
        # bot.send_photo(callback.message.chat.id, file2, 'Пёс Арчи', reply_markup= markup)
    if callback.data == 'prev':
        # file2 = open('./пёс Арчи.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        petbutton1 = types.InlineKeyboardButton('◀️', callback_data='prev')
        petbutton2 = types.InlineKeyboardButton('▶️', callback_data='next')
        petbutton3 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(petbutton1, petbutton2)
        markup.row(petbutton3)
        name, i = get_name(i, -1)
        path, description = get_pet(name)
        # name, path, description = get_pet(get_name(-1))
        file2 = open(path, 'rb')
        photo = types.InputMediaPhoto(file2)
        bot.edit_message_media(chat_id=callback.message.chat.id, message_id=callback.message.message_id, media=photo)
        bot.edit_message_caption(description, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
        # bot.send_photo(callback.message.chat.id, file2, description, reply_markup=markup)
    if callback.data == 'cats':
        i = 0
        # bot.send_message(callback.message.chat.id, 'Здесь будут объявления о кошках', parse_mode='html')
        markup = types.InlineKeyboardMarkup()
        catbutton1 = types.InlineKeyboardButton('◀️', callback_data='prev')
        catbutton2 = types.InlineKeyboardButton('▶️', callback_data='next')
        catbutton3 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(catbutton1,catbutton2)
        markup.row(catbutton3)
        # file = open('./собака Груша.jpg', 'rb')
        # bot.send_photo(callback.message.chat.id, file, 'Собака Груша\nГруше всего 8 месяцев.\nЭта очаровательная рыжая девчонка покоряет с первого взгляда- веселая, ласковая, невероятная оптимистка, ну как в такую не влюбиться ? Груша абсолютно открытый и доверчивый подросток, любит весь мир вокруг и верит, что впереди только радость. Очень любит обниматься, никогда не проявляет агрессии, нежная до невозможности, с радостью общается с другими собаками, так что готова стать и вторым питомцем в семье.', reply_markup = markup)
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
        # bot.edit_message_text(donation_text, callback.message.chat.id, callback.message.message_id)
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
        # bot.send_message(callback.message.chat.id, information.dogs_text1, reply_markup=markup)
        bot.edit_message_text(information.dogs_text1, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
        # bot.send_message(callback.message.chat.id, information.dogs_text2, reply_markup=markup)
    if callback.data == 'nextdoginfo':
        markup = types.InlineKeyboardMarkup()
        dogsinfo2button1 = types.InlineKeyboardButton('🏠', callback_data='home')
        dogsinfo2button2 = types.InlineKeyboardButton('◀️', callback_data='dogs_info')
        markup.row(dogsinfo2button2)
        markup.row(dogsinfo2button1)
        bot.edit_message_text(information.dogs_text2, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
        # bot.send_message(callback.message.chat.id, information.dogs_text2, reply_markup=markup)
    if callback.data == 'cats_info':
        markup = types.InlineKeyboardMarkup()
        catsinfobutton1 = types.InlineKeyboardButton('🏠', callback_data='home')
        markup.row(catsinfobutton1)
        bot.edit_message_text(information.cats_text, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
        # bot.send_message(callback.message.chat.id, information.cats_text, reply_markup=markup)
    if callback.data == 'home':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Собаки', callback_data='dogs')
        button2 = types.InlineKeyboardButton('Кошки', callback_data='cats')
        markup.row(button1, button2)
        button3 = types.InlineKeyboardButton('Пожертвование', callback_data='donate')
        button4 = types.InlineKeyboardButton('Полезная информация', callback_data='info')
        markup.row(button3, button4)
        # bot.edit_message_text(f'Чем мы можем вам помочь?', callback.message.chat.id, callback.message.message_id, reply_markup=markup)
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
