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
        show_symptoms(message)
    elif message.text == "/prevention":
        show_prevention(message)
    elif message.text == "/questions":
        bot.send_message(message.from_user.id, "Вопросы: в разработке!")
    elif message.text == "/news":
        bot.send_message(message.from_user.id, "Новости: в разработке!")
    elif message.text == "/develop":
        show_develop(message)
    elif message.text == "/fact":
        bot.send_message(message.from_user.id, "Факты: в разработке!")
    else:
        bot.send_message(message.from_user.id, text_of_messages.TEXT_ERROR_MESSAGE)


# Метод отправки существующих задач:
def show_bot_tasks(message):
    bot.send_message(message.from_user.id, text_of_messages.TEXT_TASKS, parse_mode="Markdown")


# Метод отправки симптомов COVID-19:
def show_symptoms(message):
    bot.send_message(message.from_user.id, text_of_messages.TEXT_SYMPTOMS, parse_mode="Markdown")


# Метод отправки профилактики COVID-19:
def show_prevention(message):
    bot.send_message(message.from_user.id, text_of_messages.TEXT_PREVENTION, parse_mode="Markdown")


# Метод отправки контактов разработчиков:
def show_develop(message):
    bot.send_message(message.from_user.id, text_of_messages.TEXT_DEVELOP, parse_mode="Markdown",
                     disable_web_page_preview=True)


# Непрерывное прослушивание пользователя:
bot.polling(none_stop=True, interval=0)
