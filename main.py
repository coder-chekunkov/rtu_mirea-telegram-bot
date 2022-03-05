import telebot
from telebot import types
import text_of_messages

# Активирование токена и запуск бота:
token = '5219565252:AAETCFyyTmY3ioY6yQr56Eiz5iTSdJ5jl4s'
bot = telebot.TeleBot(token)


# Метод отправки "приветственного сообщения"
# и вывод кнопки с возможными задачами:
@bot.message_handler(commands=['start'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_tasks = types.KeyboardButton(text=text_of_messages.TEXT_BUTTON_TASKS)
    keyboard.add(button_tasks)
    bot.send_message(message.from_user.id, text_of_messages.START_MESSAGE, reply_markup=keyboard)


# Метод "прослушивания" чата:
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == text_of_messages.TEXT_BUTTON_TASKS:
        show_bot_tasks(message)
    elif message.text == "/stat":
        bot.send_message(message.from_user.id, "Статистика: в разработке!")
    elif message.text == "/symptoms":
        bot.send_message(message.from_user.id, "Симптомы: в разработке!")
    elif message.text == "/prevention":
        bot.send_message(message.from_user.id, "Профилактика: в разработке!")
    elif message.text == "/questions":
        bot.send_message(message.from_user.id, "Вопросы: в разработке!")
    elif message.text == "/develop":
        bot.send_message(message.from_user.id, "Разработчики: в разработке!")
    elif message.text == "/fact":
        bot.send_message(message.from_user.id, "Факты: в разработке!")
    else:
        bot.send_message(message.from_user.id, text_of_messages.TEXT_ERROR_MESSAGE)


# Метод отправки существующих задач:
def show_bot_tasks(message):
    bot.send_message(message.from_user.id, text_of_messages.TEXT_TASKS, parse_mode="Markdown")


# Непрерывное прослушивание пользователя:
bot.polling(none_stop=True, interval=0)
bot.idle()
