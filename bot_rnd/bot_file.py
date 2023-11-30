"""Создать бота, который будет загадывать цифру
затем придлагать клавиатуру с 5 кнопками,
в одном из них загаданное программой число
После ввода одного из них нужно выводить соотвтествующие сообщения:
1) Угадал!
2) Не угадал
"""
import telebot
import random
TOKEN = '6958334794:AAHDu5XcL8Orct8XO14eMnxA1SRBqMv9auU'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я загадаю число от 1 до 5. Попробуй угадать!")

    # Загадываем число
    bot.random_number = random.randint(1, 5)

    # Показываем клавиатуру
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [str(i) for i in range(1, 6)]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выбери число или отправь /end, чтобы завершить раунд:", reply_markup=markup)

@bot.message_handler(commands=['end'])
def handle_end(message):

    bot.send_message(message.chat.id, "Раунд завершен. Чтобы начать новый, отправь /start.")

@bot.message_handler(func=lambda message: True)
def handle_guess(message):
    try:
        guessed_number = int(message.text)

        if guessed_number == bot.random_number:
            bot.send_message(message.chat.id, "Угадал!")
        else:
            bot.send_message(message.chat.id, "Не угадал!")

        # Убираем клавиатуру
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "Раунд завершен. Чтобы начать новый, отправь /start.", reply_markup=markup)

    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, выбери число, используя клавиатуру, или отправь /end, чтобы завершить раунд.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
