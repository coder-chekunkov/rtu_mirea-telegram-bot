import telebot

# Активирование токена и запуск бота:
token = '5219565252:AAETCFyyTmY3ioY6yQr56Eiz5iTSdJ5jl4s'
bot = telebot.TeleBot(token)


# Тестовый метод:
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "what ")


# Непрерывное прослушивание пользователя:
bot.polling(none_stop=True, interval=0)
