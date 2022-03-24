import telebot
import emoji
from telebot import types
from covid_19_worker.JSON_worker.question import questions_creator
from covid_19_worker.BS_worker.news.interfax import news_interfax_creator
from covid_19_worker.BS_worker.news.yandex import news_yandex_creator
from covid_19_worker import covid_creator
from static_worker import text_creator
# from BS_worker.statistic.world import world_statistic_creator
# from BS_worker.statistic.russia import russia_statistic_creator
# from BS_worker.news.google import news_google_creator

# Активирование токена и запуск бота:
token = '5219565252:AAETCFyyTmY3ioY6yQr56Eiz5iTSdJ5jl4s'
bot = telebot.TeleBot(token)

# Текст для вывода задач:
TEXT_BUTTON_TASKS = "Посмотреть доступные задачи " + emoji.emojize(
    ":card_index_dividers:")

all_users = set()


# Метод отправки "приветственного сообщения"
# и вывод кнопки с возможными задачами:
@bot.message_handler(commands=['start'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_tasks = types.KeyboardButton(text=TEXT_BUTTON_TASKS)
    keyboard.add(button_tasks)
    START_MESSAGE = text_creator.get_text("start_message")
    bot.send_message(message.from_user.id, START_MESSAGE,
                     reply_markup=keyboard, parse_mode="Markdown")
    all_users.add(message.from_user.id)
    print(all_users)


# Метод "прослушивания" чата:
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == TEXT_BUTTON_TASKS:
        # Посмотреть все разделы бота:
        show_tasks(message)
    elif message.text == "/develop":
        # Все о разработчиках:
        show_develop(message)
    elif message.text == "/covid":
        covid_creator.show_bot_tasks(message, bot)
    elif message.text == "/stat":
        # Статистика covid_19_worker-19:
        covid_creator.show_statistic(message, telebot, bot)
    elif message.text == "/symptoms":
        # Симптомы covid_19_worker-19:
        covid_creator.show_symptoms(message, bot)
    elif message.text == "/prevention":
        # Профилактика covid_19_worker-19:
        covid_creator.show_prevention(message, bot)
    elif message.text == "/questions":
        # Вопросы/ответы covid_19_worker-19:
        covid_creator.show_questions(message, telebot, bot)
    elif message.text == "/newscovid":
        # Новости covid_19_worker-19:
        covid_creator.show_news(message, telebot, bot)
    elif message.text == "/fact":
        # Факты covid_19_worker-19:
        covid_creator.show_fact(message, bot)
    else:
        # Сообщение об ошибке:
        TEXT_ERROR_MESSAGE = text_creator.get_text("error")
        bot.send_message(message.from_user.id, TEXT_ERROR_MESSAGE)


# Метод отправки всех доступных разделов:
def show_tasks(message):
    TEXT_TASKS = text_creator.get_text("tasks")
    bot.send_message(message.from_user.id, TEXT_TASKS, parse_mode="Markdown",
                     disable_web_page_preview=True)


# Метод отправки контактов разработчиков:
def show_develop(message):
    TEXT_DEVELOP = text_creator.get_text("develop")
    bot.send_message(message.from_user.id, TEXT_DEVELOP, parse_mode="Markdown",
                     disable_web_page_preview=True)


# Обработчик нажатия на кнопку:
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data != "russia" and call.data != "world" and call.data != "google" and call.data != "interfax" and call.data != "yandex":
        number_of_question = call.data
        answer, question = questions_creator.answers_print(number_of_question)
        message = "⁉️ *Ответ на вопрос №" + number_of_question + ":* " + question + "\n" + " " + "\n" + answer + \
                  "\n" + " " + "\n" + "🤤 Нажмите на другую кнопку, чтобы получить ответ на следующий вопрос."
        bot.send_message(chat_id=call.message.chat.id, text=message,
                         parse_mode="Markdown")
    else:
        if call.data == "russia":
            bot.send_message(chat_id=call.message.chat.id,
                             text="Technical works.", parse_mode="Markdown")
            # message_russia, message_region = russia_statistic_creator.show_stat_russia()
            # bot.send_message(chat_id=call.message.chat.id, text=message_russia,
            #                  parse_mode="Markdown")
            # bot.send_message(chat_id=call.message.chat.id, text=message_region,
            #                  parse_mode="Markdown")
        if call.data == "world":
            bot.send_message(chat_id=call.message.chat.id,
                             text="Technical works.", parse_mode="Markdown")
            # message_world, message_countries = world_statistic_creator.show_stat_world()
            # bot.send_message(chat_id=call.message.chat.id, text=message_world,
            #                  parse_mode="Markdown")
            # bot.send_message(chat_id=call.message.chat.id,
            #                  text=message_countries, parse_mode="Markdown")

        if call.data == "google":
            bot.send_message(chat_id=call.message.chat.id,
                             text="Technical works.", parse_mode="Markdown")
            # message_news_google = news_google_creator.get_google_news()
            # bot.send_message(chat_id=call.message.chat.id,
            #                  text=message_news_google, parse_mode="Markdown",
            #                  disable_web_page_preview=True)
        if call.data == "interfax":
            message_news_interfax = news_interfax_creator.get_interfax_news()
            bot.send_message(chat_id=call.message.chat.id,
                             text=message_news_interfax, parse_mode="Markdown",
                             disable_web_page_preview=True)
        if call.data == "yandex":
            message_news_google = news_yandex_creator.get_yandex_news()
            bot.send_message(chat_id=call.message.chat.id,
                             text=message_news_google, parse_mode="Markdown",
                             disable_web_page_preview=True)


# Непрерывное прослушивание пользователя:
# my_thread = threading.Thread(target=check_time)
# my_thread.start()
bot.polling(none_stop=True, interval=0)
