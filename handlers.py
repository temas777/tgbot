import telebot
token='5005657511:AAHKWoVnEYC8N7x5gbe_eJiCHaO_8Gdof8Y'
bot=telebot.Telebot(token)
@bot.message_handler(commands=['t'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_poling()
