import threading
import time
import schedule
import telebot
import emoji
from telebot import types
from src.covid_19_worker.JSON_worker.question import questions_creator
from src.covid_19_worker.BS_worker.news.interfax import news_interfax_creator
from src.covid_19_worker.BS_worker.news.yandex import news_yandex_creator
from src.covid_19_worker import covid_creator
from src.static_worker import text_creator
from src.university_worker import univercity_creator
from src.covid_19_worker.BS_worker.statistic.world import \
    world_statistic_creator
from src.covid_19_worker.BS_worker.statistic.russia import \
    russia_statistic_creator
from src.covid_19_worker.BS_worker.statistic.rtu_mirea import rtu_mirea_creator
from src.covid_19_worker.BS_worker.news.rbk import news_google_creator
from src.news_worker.news_mirea import news_creator
from src.news_worker.word_checker import word_searcher
from src.news_worker import news_shower
from src.news_worker.word_checker import university_searcher
from src.log_worker import log_creator

# Активирование токена и запуск бота:
token = '5219565252:AAETCFyyTmY3ioY6yQr56Eiz5iTSdJ5jl4s'
bot = telebot.TeleBot(token)

# Текст для вывода задач:
TEXT_BUTTON_TASKS = "Главное Меню " + emoji.emojize(
    ":card_index_dividers:")

all_users = set()
global word_search
global news_index


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

    # Создание лога:
    log_creator.make_log(message, "присоединение/перезапуск")


# Метод "прослушивания" чата:
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == TEXT_BUTTON_TASKS:
        # Посмотреть все разделы бота:
        show_tasks(message)
    elif message.text == "/menu":
        # Посмотреть все разделы бота:
        show_tasks(message)
    elif message.text == "/develop":
        # Все о разработчиках:
        show_develop(message)
    elif message.text == "/covid":
        # Все возможные задачи с "COVID-19":
        covid_creator.show_bot_tasks(message, telebot, bot)
    elif message.text == "/news":
        # Новости с РТУ МИРЭА:
        news_shower.show_dates_button(message, telebot, bot)
    elif message.text == "/university":
        # Информация о институтах и кафедр:
        univercity_creator.show_buttons_university(message, telebot, bot)
    else:
        show_message_counter(message)


# Метод отправки всех доступных разделов:
def show_tasks(message):
    TEXT_TASKS = text_creator.get_text("tasks")
    bot.send_message(message.from_user.id, TEXT_TASKS, parse_mode="Markdown",
                     disable_web_page_preview=True)

    # Создание лога:
    log_creator.make_log(message, "переход в \"Главное меню\"")


# Метод отправки контактов разработчиков:
def show_develop(message):
    TEXT_DEVELOP = text_creator.get_text("develop")
    bot.send_message(message.from_user.id, TEXT_DEVELOP, parse_mode="Markdown",
                     disable_web_page_preview=True)

    # Создание лога:
    log_creator.make_log(message, "переход в \"Разработчики\"")


# Метод отправки клавиатуры с уточнением задачи:
def show_message_counter(message):
    global word_search
    word_search = " "
    word_search = message.text
    TEXT_MESSAGE_WORD = "🔍 Искать слово *" + word_search + "* в новостях?"
    TEXT_BUTTON_YES = "Да ✅"
    TEXT_BUTTON_NO = "Нет ❌"

    keyboard_word_checker = telebot.types.InlineKeyboardMarkup()
    button_yes = telebot.types.InlineKeyboardButton(
        text=TEXT_BUTTON_YES, callback_data="word_checker_yes",
        parse_mode="Markdown")
    button_no = telebot.types.InlineKeyboardButton(
        text=TEXT_BUTTON_NO, callback_data="word_checker_no",
        parse_mode="Markdown")

    keyboard_word_checker.add(button_yes, button_no)
    bot.send_message(message.from_user.id,
                     TEXT_MESSAGE_WORD,
                     reply_markup=keyboard_word_checker, parse_mode="Markdown")

    # Создание лога:
    text_message_log = "ввод слова \"" + word_search + "\""
    log_creator.make_log(message, text_message_log)


def show_keyboard_news_university(call, university):
    global news_index
    news_index = []
    news_index = university_searcher.university_search(university)
    counter = len(news_index)
    message_counter = "🔃 Количество упоминаний в новостях: " + str(
        counter)
    bot.send_message(chat_id=call.message.chat.id,
                     text=message_counter, parse_mode="Markdown")

    keyboard_show_news = telebot.types.InlineKeyboardMarkup()
    TEXT_MESSAGE_WORD = "🔍 Показать данные новости?"
    TEXT_BUTTON_YES = "Да ✅"
    TEXT_BUTTON_NO = "Нет ❌"

    button_yes = telebot.types.InlineKeyboardButton(text=TEXT_BUTTON_YES,
                                                    callback_data="show_news_university_yes",
                                                    parse_mode="Markdown")
    button_no = telebot.types.InlineKeyboardButton(text=TEXT_BUTTON_NO,
                                                   callback_data="show_news_university_no",
                                                   parse_mode="Markdown")
    keyboard_show_news.add(button_yes, button_no)
    bot.send_message(chat_id=call.message.chat.id, text=TEXT_MESSAGE_WORD,
                     reply_markup=keyboard_show_news,
                     parse_mode="Markdown")


# Обработчик нажатия на кнопку:
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    global news_index
    if call.data == "statistic":
        # Статистика covid_19_worker-19:
        covid_creator.show_statistic(call, telebot, bot)

        # Создание лога:
        log_creator.make_log(call, "запрос статистики \"COVID-19\"")

    elif call.data == "newscovid":
        # Новости covid_19_worker-19:
        covid_creator.show_news(call, telebot, bot)

        # Создание лога:
        log_creator.make_log(call, "запрос новостей по \"COVID-19\"")

    elif call.data == "symptoms":
        # Симптомы covid_19_worker-19:
        covid_creator.show_symptoms(call, bot)

        # Создание лога:
        log_creator.make_log(call, "запрос симптомов по \"COVID-19\"")

    elif call.data == "prevention":
        # Профилактика covid_19_worker-19:
        covid_creator.show_prevention(call, bot)

        # Создание лога:
        log_creator.make_log(call, "запрос профилактики \"COVID-19\"")

    elif call.data == "questions":
        # Вопросы/ответы covid_19_worker-19:
        covid_creator.show_questions(call, telebot, bot)

        # Создание лога:
        log_creator.make_log(call, "запрос вопросов/ответов по \"COVID-19\"")

    elif call.data == "facts":
        # Факты covid_19_worker-19:
        covid_creator.show_fact(call, bot)

        # Создание лога:
        log_creator.make_log(call, "запрос факта по \"COVID-19\"")

    elif call.data == "russia":
        # Вывод статистики заболеваемости по России:
        message_russia, message_region = russia_statistic_creator.show_stat_russia()
        bot.send_message(chat_id=call.message.chat.id, text=message_russia,
                         parse_mode="Markdown")
        bot.send_message(chat_id=call.message.chat.id, text=message_region,
                         parse_mode="Markdown")

        # Создание лога:
        log_creator.make_log(call, "запрос статистики заболеваемости "
                                   "\"COVID-19\" по России")

    elif call.data == "world":
        # Вывод статистики заболеваемости по Миру:
        message_countries = world_statistic_creator.show_stat_world()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_countries, parse_mode="Markdown")

        # Создание лога:
        log_creator.make_log(call, "запрос статистики заболеваемости "
                                   "\"COVID-19\" по Миру")

    elif call.data == "mirea_stat":
        # Вывод статистики заболеваемости по РТУ МИРЭА:
        message_title, message_stat = rtu_mirea_creator.get_statistic_mirea()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_title, parse_mode="Markdown")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_stat, parse_mode="Markdown")

        # Создание лога:
        log_creator.make_log(call, "запрос статистики заболеваемости "
                                   "\"COVID-19\" по РТУ МИРЭА")

    elif call.data == "last_10_news":
        # Парсинг и вывод последних 10 новостей:
        news_creator.show_mirea_news(call, bot, 10)

        # Создание лога:
        log_creator.make_log(call, "запрос последних 10 новостей по \"РТУ "
                                   "МИРЭА\"")

    elif call.data == "last_20_news":
        # Парсинг и вывод последних 20 новостей:
        news_creator.show_mirea_news(call, bot, 20)

        # Создание лога:
        log_creator.make_log(call, "запрос последних 20 новостей по \"РТУ "
                                   "МИРЭА\"")

    elif call.data == "last_30_news":
        # Парсинг и вывод последних 30 новостей:
        news_creator.show_mirea_news(call, bot, 30)

        # Создание лога:
        log_creator.make_log(call, "запрос последних 30 новостей по \"РТУ "
                                   "МИРЭА\"")

    elif call.data == "last_40_news":
        # Парсинг и вывод последних 30 новостей:
        news_creator.show_mirea_news(call, bot, 40)

        # Создание лога:
        log_creator.make_log(call, "запрос последних 40 новостей по \"РТУ "
                                   "МИРЭА\"")

    elif call.data == "update_news":
        # Принудительное обновление новостей:
        TEXT_MESSAGE_START_UPDATE = "🔃 Обновление новостей \"*РТУ МИРЭА*\" началось."
        bot.send_message(chat_id=call.message.chat.id,
                         text=TEXT_MESSAGE_START_UPDATE, parse_mode="Markdown")
        TEXT_MESSAGE_WARNING = "⚠️Обновление *займет какое-то время*. Бот " \
                               "*сообщит* как закончит работу."
        bot.send_message(chat_id=call.message.chat.id,
                         text=TEXT_MESSAGE_WARNING, parse_mode="Markdown")

        news_creator.start_parse_pages(11)
        TEXT_MESSAGE_UPDATED = "🔃 Новости \"*РТУ МИРЭА*\" обновились."
        bot.send_message(chat_id=call.message.chat.id,
                         text=TEXT_MESSAGE_UPDATED, parse_mode="Markdown")

        # Создание лога:
        log_creator.make_log(call, "принудительное обновление новостей \"РТУ "
                                   "МИРЭА\"")

    elif call.data == "rbk":
        # Получение новостей с сайта "rbk":
        message_news_google = news_google_creator.get_google_news()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_news_google, parse_mode="Markdown",
                         disable_web_page_preview=True)

        # Создание лога:
        log_creator.make_log(call, "запрос новостей по \"COVID-19\" с rbk")

    elif call.data == "interfax":
        # Получение новостей с сайта "interfax":
        message_news_interfax = news_interfax_creator.get_interfax_news()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_news_interfax, parse_mode="Markdown",
                         disable_web_page_preview=True)

        # Создание лога:
        log_creator.make_log(call, "запрос новостей по \"COVID-19\" с "
                                   "interfax")

    elif call.data == "yandex":
        # Получение новостей с сайта "yandex":
        message_news_google = news_yandex_creator.get_yandex_news()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_news_google, parse_mode="Markdown",
                         disable_web_page_preview=True)

        # Создание лога:
        log_creator.make_log(call, "запрос новостей по \"COVID-19\" с yandex")

    elif call.data == "word_checker_yes":
        # Вывод сообщения о подсчете слова:
        word_searcher.news_search(call, bot, word_search)

        # Создание лога:
        text_message_log = "запрос подсчета слова \"" + word_search + "\""
        log_creator.make_log(call, text_message_log)

    elif call.data == "word_checker_no":
        # Сообщение об ошибке:
        TEXT_ERROR_MESSAGE = text_creator.get_text("error")
        bot.send_message(chat_id=call.message.chat.id,
                         text=TEXT_ERROR_MESSAGE, parse_mode="Markdown")

        # Создание лога:
        log_creator.make_log(call, "переход в \"Главное меню\"")

    elif call.data == "university_0":
        # Институт Информационных Технологий:
        message_about_university = univercity_creator.get_information("three")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        show_keyboard_news_university(call, "IT")

        # Создание лога:
        log_creator.make_log(call, "вывод информации о институте \"ИТ\"")

    elif call.data == "university_1":
        # Институт искусственного интеллекта:
        message_about_university = univercity_creator.get_information("three")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        show_keyboard_news_university(call, "II")

        # Создание лога:
        log_creator.make_log(call, "вывод информации о институте \"ИИ\"")

    elif call.data == "university_2":
        # Институт кибербезопасности и цифровых технологий:
        message_about_university = univercity_creator.get_information("three")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        show_keyboard_news_university(call, "CADT")

        # Создание лога:
        log_creator.make_log(call, "вывод информации о институте \"КИЦТ\"")

    elif call.data == "university_3":
        # Институт перспективных технологий и индустриального программирования:
        message_about_university = univercity_creator.get_information("four")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        show_keyboard_news_university(call, "ATIP")

        # Создание лога:
        log_creator.make_log(call, "вывод информации о институте \"ПТИП\"")

    elif call.data == "university_4":
        # Институт радиоэлектроники и информатики:
        message_about_university = univercity_creator.get_information("five")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        show_keyboard_news_university(call, "REI")

        # Создание лога:
        log_creator.make_log(call, "вывод информации о институте \"РЭИ\"")

    elif call.data == "university_5":
        # Институт технологий управления:
        message_about_university = univercity_creator.get_information("six")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        show_keyboard_news_university(call, "MT")

        # Создание лога:
        log_creator.make_log(call, "вывод информации о институте \"ТУ\"")

    elif call.data == "university_6":
        # Институт тонких химических технологий им. М.В. Ломоносова:
        message_about_university = univercity_creator.get_information("seven")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        show_keyboard_news_university(call, "FCTL")

        # Создание лога:
        log_creator.make_log(call, "вывод информации о институте \"ИМХТ\"")

    elif call.data == "show_news_university_yes":
        # Вывод всех новостей с упоминанием института:
        university_searcher.news_output(call, bot, news_index)

        # Создание лога:
        log_creator.make_log(call, "вывод новостей с институтами")

    elif call.data == "show_news_university_no":
        # Отказ смотреть новости с институтами:
        show_tasks(call)
        # Создание лога:
        log_creator.make_log(call, "отказ выводить новости с институтами")

    else:
        number_of_question = call.data
        answer, question = questions_creator.answers_print(number_of_question)
        message = "⁉️ *Ответ на вопрос №" + number_of_question + ":* " + question + "\n" + " " + "\n" + answer + \
                  "\n" + " " + "\n" + "🤤 Нажмите на другую кнопку, чтобы получить ответ на следующий вопрос."
        bot.send_message(chat_id=call.message.chat.id, text=message,
                         parse_mode="Markdown")

        # Создание лога:
        log_creator.make_log(call, "запрос ответа на вопрос по \"COVID-19\"")


# Проверка времени:
def check_time():
    schedule.every().day.at("11:37").do(show_every_day_message_stat)
    schedule.every().day.at("11:38").do(show_every_day_message_news)
    schedule.every().day.at("15:00").do(show_every_day_message_news)
    schedule.every().day.at("19:00").do(show_every_day_message_news)
    schedule.every().day.at("22:00").do(show_every_day_message_news)
    while True:
        schedule.run_pending()
        time.sleep(1)


# Метод вывода ежедневного сообщения с обновленными новостями РТУ МИРЭА:
def show_every_day_message_news():
    # Создание лога:
    log_creator.make_log_bot("Автоматическое обновление новостей \"РТУ "
                             "МИРЭА\"")

    news_creator.start_parse_pages(11)
    TEXT_MESSAGE = "🔃 Новости \"*РТУ МИРЭА*\" обновились."
    for user in all_users:
        bot.send_message(user, TEXT_MESSAGE, parse_mode="Markdown")


# Метод вывода ежедневного сообщения с обновленной статисткой заболеваемости:
def show_every_day_message_stat():
    # Создание лога:
    log_creator.make_log_bot("Автоматическое обновление статистики "
                             "заболеваемости \"COVID-19\"")

    russia_statistic_creator.get_statistic_russia()
    world_statistic_creator.get_statistic_world()
    rtu_mirea_creator.get_statistic_mirea()

    TEXT_MESSAGE = "📊 Статистка заболеваемости *COVID-19* обновилась."
    for user in all_users:
        bot.send_message(user, TEXT_MESSAGE, parse_mode="Markdown")


# Непрерывное прослушивание пользователя:
my_thread = threading.Thread(target=check_time)
my_thread.start()
bot.polling(none_stop=True, interval=0)
