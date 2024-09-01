import telebot
import webbrowser

bot = telebot.TeleBot('7228654217:AAERzZ662cate8coueeC__DFm8Xbg0_CQb8')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://github.com/Vasiliy-moroshka/bot_project_br')
@bot.message_handler(commands=['start', 'hello', 'main'])

def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])

def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID, {message.from_user.id}')

bot.polling(none_stop=True)