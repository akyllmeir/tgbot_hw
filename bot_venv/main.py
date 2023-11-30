from env import BOT_TOKEN
import telebot

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['info'])
def info_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "get stick bugged lol.")

if __name__ == "__main__":
    bot.polling(none_stop=True)