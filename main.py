import telebot
from telebot import types
from static_worker import text_of_messages
from JSON_worker.question import questions_creator
from JSON_worker.fact import facts_creator

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
        show_questions(message)
    elif message.text == "/news":
        bot.send_message(message.from_user.id, "Новости: в разработке!")
    elif message.text == "/develop":
        show_develop(message)
    elif message.text == "/fact":
        show_fact(message)
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


# Метод вывода всех доступных вопросов:
def show_questions(message):
    bot.send_message(message.from_user.id, questions_creator.questions_print(), parse_mode="Markdown")


# Метод вывода одного интересного факта:
def show_fact(message):
    bot.send_message(message.from_user.id, facts_creator.facts_print(), parse_mode="Markdown")


# Непрерывное прослушивание пользователя:
bot.polling(none_stop=True, interval=0)
