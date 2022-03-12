import telebot
import emoji
from telebot import types
from static_worker import tags_cheking
from JSON_worker.question import questions_creator
from JSON_worker.fact import facts_creator
from JSON_worker.text import text_creator

# Активирование токена и запуск бота:
token = '5219565252:AAETCFyyTmY3ioY6yQr56Eiz5iTSdJ5jl4s'
bot = telebot.TeleBot(token)

# Текст для вывода задач:
TEXT_BUTTON_TASKS = "Посмотреть доступные задачи " + emoji.emojize(":card_index_dividers:")


# Метод отправки "приветственного сообщения"
# и вывод кнопки с возможными задачами:
@bot.message_handler(commands=['start'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_tasks = types.KeyboardButton(text=TEXT_BUTTON_TASKS)
    keyboard.add(button_tasks)
    START_MESSAGE = text_creator.get_text("start_message")
    bot.send_message(message.from_user.id, START_MESSAGE, reply_markup=keyboard)


# Метод "прослушивания" чата:
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == TEXT_BUTTON_TASKS:
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
        show_answer(message)


# Метод отправки существующих задач:
def show_bot_tasks(message):
    TEXT_TASKS = text_creator.get_text("tasks")
    bot.send_message(message.from_user.id, TEXT_TASKS, parse_mode="Markdown")


# Метод отправки симптомов COVID-19:
def show_symptoms(message):
    TEXT_SYMPTOMS = text_creator.get_text("symptoms")
    bot.send_message(message.from_user.id, TEXT_SYMPTOMS, parse_mode="Markdown")


# Метод отправки профилактики COVID-19:
def show_prevention(message):
    TEXT_PREVENTION = text_creator.get_text("prevention")
    bot.send_message(message.from_user.id, TEXT_PREVENTION, parse_mode="Markdown")


# Метод отправки контактов разработчиков:
def show_develop(message):
    TEXT_DEVELOP = text_creator.get_text("develop")
    bot.send_message(message.from_user.id, TEXT_DEVELOP, parse_mode="Markdown",
                     disable_web_page_preview=True)


# Метод вывода всех доступных вопросов:
def show_questions(message):
    TEXT_QUESTIONS = questions_creator.questions_print()
    bot.send_message(message.from_user.id, TEXT_QUESTIONS, parse_mode="Markdown")


# Метод вывода одного интересного факта:
def show_fact(message):
    TEXT_FACT = facts_creator.facts_print()
    bot.send_message(message.from_user.id, TEXT_FACT, parse_mode="Markdown")


# Метод вывода сообщения с дальнейшими действиями:
def show_answer(message):
    # Текст для ввода "Да":
    TEXT_BUTTON_YES = "Да " + emoji.emojize("✅")

    # Текст для ввода "Нет":
    TEXT_BUTTON_NO = "Нет " + emoji.emojize("❌")

    isFoundTag, tag = tags_cheking.tag_finder(message.text)
    if isFoundTag:
        # Запись конечного вопроса пользователю, в зависимости от тега:
        buff_message = ""
        if tag == "статистика":
            buff_message = emoji.emojize(":bar_chart:") + " Вы хотите посмотреть статистику?"
        elif tag == "новости":
            buff_message = emoji.emojize(":bookmark_tabs:") + " Вы хотите посмотреть актуальные новости?"
        elif tag == "симптомы":
            buff_message = emoji.emojize("🤕") + " Вы хотите узнать о симптомах COVID-19?"
        elif tag == "профилактика":
            buff_message = emoji.emojize("😷") + " Вы хотите узнать о профилактики?"
        elif tag == "вопросы":
            buff_message = emoji.emojize("⁉️") + " Показать часто задаваемые вопросы?"
        elif tag == "факт":
            buff_message = emoji.emojize("🤔") + " Показать интересный факт?"
        elif tag == "разработчики":
            buff_message = emoji.emojize("🤔") + " Показать контакты разработчиков?"

        # Вывод вопроса и двух кнопок "да" или "нет":
        keyboard_YES_NO = telebot.types.InlineKeyboardMarkup()
        button_YES = telebot.types.InlineKeyboardButton(TEXT_BUTTON_YES, callback_data='1',
                                                        parse_mode="Markdown")
        button_NO = telebot.types.InlineKeyboardButton(TEXT_BUTTON_NO, callback_data='2',
                                                       parse_mode="Markdown")
        keyboard_YES_NO.row(button_YES, button_NO)
        bot.send_message(message.from_user.id, buff_message,
                         reply_markup=keyboard_YES_NO)
    else:
        TEXT_ERROR_MESSAGE = text_creator.get_text("error")
        bot.send_message(message.from_user.id, TEXT_ERROR_MESSAGE)


# Непрерывное прослушивание пользователя:
bot.polling(none_stop=True, interval=0)
