import telebot

bot = telebot.TeleBot('7228654217:AAERzZ662cate8coueeC__DFm8Xbg0_CQb8')

@bot.message_handler(commands=['start', 'hello', 'main'])

def main(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['help'])

def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

bot.polling(none_stop=True)