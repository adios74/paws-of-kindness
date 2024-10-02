import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('7063861683:AAEj42JKRsa2Qst1aigI9VyK4wX3EfzFfG8')


@bot.message_handler(command=['site', 'website'])
def site(message):
    webbrowser.open('https://vsemposobake.ru')

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Объявления о собаках', callback_data='dogs')
    button2 = types.InlineKeyboardButton('Объявления о кошках', callback_data='cats')
    markup.row(button1, button2)
    button3 = types.InlineKeyboardButton('Сделать пожертвование', callback_data='donate')
    button4 = types.InlineKeyboardButton('Памятка владельцу собаки', url='https://vsemposobake.ru/wp-content/uploads/2018/07/Pamyatka_new.pdf')
    markup.row(button3, button4)
    button5 = types.InlineKeyboardButton('Полезная информация', callback_data='info')
    markup.row(button5)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Чем мы можем вам помочь?', reply_markup = markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'dogs':
        file = open('./собака Груша.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        dogbutton1 = types.InlineKeyboardButton('❤️', callback_data='liked1')
        dogbutton2 = types.InlineKeyboardButton('▶️', callback_data='next1')
        dogbutton3 = types.InlineKeyboardButton('◀️', callback_data='back')
        dogbutton4 = types.InlineKeyboardButton('❌', callback_data='exit')
        markup.row(dogbutton3, dogbutton2)
        markup.row(dogbutton1, dogbutton4)
        bot.send_photo(callback.message.chat.id, file, 'Собака Груша: Груше всего 8 месяцев. Эта очаровательная рыжая девчонка покоряет с первого взгляда- веселая, ласковая, невероятная оптимистка, ну как в такую не влюбиться ? Груша абсолютно открытый и доверчивый подросток, любит весь мир вокруг и верит, что впереди только радость. Очень любит обниматься, никогда не проявляет агрессии, нежная до невозможности, с радостью общается с другими собаками, так что готова стать и вторым питомцем в семье.', reply_markup = markup)
    if callback.data == 'liked1':
        bot.send_message(callback.message.chat.id, 'Волонтёр: Екатерина. Контактный телефон: +79775796172 Приют: Бирюлево', parse_mode='html')
    if callback.data == 'next1':
        file2 = open('./пёс Арчи.jpg', 'rb')
        markup = types.InlineKeyboardMarkup()
        dogbutton1 = types.InlineKeyboardButton('❤️', callback_data='liked2')
        dogbutton2 = types.InlineKeyboardButton('▶️', callback_data='next2')
        dogbutton3 = types.InlineKeyboardButton('◀️', callback_data='back1')
        dogbutton4 = types.InlineKeyboardButton('❌', callback_data='exit')
        markup.row(dogbutton3, dogbutton2)
        markup.row(dogbutton1, dogbutton4)
        bot.send_photo(callback.message.chat.id, file2, 'Пёс Арчи', reply_markup= markup)
    if callback.data == 'back':
        bot.send_message(callback.message)
    if callback.data == 'cats':
        bot.send_message(callback.message.chat.id, 'Здесь будут объявления о кошках', parse_mode='html')
    if callback.data == 'donate':
        bot.send_message(callback.message.chat.id, 'Здесь будут ссылки на донаты', parse_mode='html')
    if callback.data == 'info':
        bot.send_message(callback.message.chat.id, 'Полезные ссылки и статьи для владельцев животных из приютов', parse_mode='html')
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}!', parse_mode='html')
    elif message.text.lower() == 'помощь':
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}!', parse_mode='html')

bot.polling(non_stop=True)