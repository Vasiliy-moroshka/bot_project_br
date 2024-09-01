import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('7228654217:AAERzZ662cate8coueeC__DFm8Xbg0_CQb8')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['site', 'website'])  # command to open a website
def site(message):
    webbrowser.open('https://github.com/Vasiliy-moroshka/bot_project_br')


@bot.message_handler(commands=['start', 'hello', 'main'])  # command to say hello to user
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])  # command to show help information
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


@bot.message_handler()  # Command to say user hello with his/her name and tell his/her id
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID, {message.from_user.id}')


@bot.message_handler(content_types=['photo', ''])  # Command for response about received photos and other files
def get_file(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://github.com/Vasiliy-moroshka')
    markup.row(btn1)  # .row create a row to arrange the buttons
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')  # inlineKeyBoardButton create a buttons
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)


bot.polling(none_stop=True)
