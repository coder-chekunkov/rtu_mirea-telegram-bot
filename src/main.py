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
from src.news_worker import news_shower

# Активирование токена и запуск бота:
token = '5219565252:AAETCFyyTmY3ioY6yQr56Eiz5iTSdJ5jl4s'
bot = telebot.TeleBot(token)

# Текст для вывода задач:
TEXT_BUTTON_TASKS = "Главное Меню " + emoji.emojize(
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
    elif message.text == "/schedule":
        # Расписание:
        show_schedule(message)
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


# Метод отправки расписания:
def show_schedule(message):
    TEXT_SCHEDULE = "В разработке!"
    bot.send_message(message.from_user.id, TEXT_SCHEDULE,
                     parse_mode="Markdown",
                     disable_web_page_preview=True)


# Обработчик нажатия на кнопку:
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data == "statistic":
        # Статистика covid_19_worker-19:
        covid_creator.show_statistic(call, telebot, bot)
    elif call.data == "newscovid":
        # Новости covid_19_worker-19:
        covid_creator.show_news(call, telebot, bot)
    elif call.data == "symptoms":
        # Симптомы covid_19_worker-19:
        covid_creator.show_symptoms(call, bot)
    elif call.data == "prevention":
        # Профилактика covid_19_worker-19:
        covid_creator.show_prevention(call, bot)
    elif call.data == "questions":
        # Вопросы/ответы covid_19_worker-19:
        covid_creator.show_questions(call, telebot, bot)
    elif call.data == "facts":
        # Факты covid_19_worker-19:
        covid_creator.show_fact(call, bot)
    elif call.data == "russia":
        # Вывод статистики заболеваемости по России:
        message_russia, message_region = russia_statistic_creator.show_stat_russia()
        bot.send_message(chat_id=call.message.chat.id, text=message_russia,
                         parse_mode="Markdown")
        bot.send_message(chat_id=call.message.chat.id, text=message_region,
                         parse_mode="Markdown")
    elif call.data == "world":
        # Вывод статистики заболеваемости по Миру:
        message_countries = world_statistic_creator.show_stat_world()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_countries, parse_mode="Markdown")
    elif call.data == "mirea_stat":
        # Вывод статистики заболеваемости по РТУ МИРЭА:
        message_title, message_stat = rtu_mirea_creator.get_statistic_mirea()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_title, parse_mode="Markdown")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_stat, parse_mode="Markdown")
    elif call.data == "last_10_news":
        # Парсинг и вывод последних 10 новостей:
        news_creator.show_mirea_news(call, bot, 10)
    elif call.data == "last_20_news":
        # Парсинг и вывод последних 20 новостей:
        news_creator.show_mirea_news(call, bot, 20)
    elif call.data == "last_30_news":
        # Парсинг и вывод последних 30 новостей:
        news_creator.show_mirea_news(call, bot, 30)
    elif call.data == "last_40_news":
        # Парсинг и вывод последних 30 новостей:
        news_creator.show_mirea_news(call, bot, 40)
    elif call.data == "rbk":
        # Получение новостей с сайта "rbk":
        message_news_google = news_google_creator.get_google_news()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_news_google, parse_mode="Markdown",
                         disable_web_page_preview=True)
    elif call.data == "interfax":
        # Получение новостей с сайта "interfax":
        message_news_interfax = news_interfax_creator.get_interfax_news()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_news_interfax, parse_mode="Markdown",
                         disable_web_page_preview=True)
    elif call.data == "yandex":
        # Получение новостей с сайта "yandex":
        message_news_google = news_yandex_creator.get_yandex_news()
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_news_google, parse_mode="Markdown",
                         disable_web_page_preview=True)
    elif call.data == "university_0":
        message_about_university = univercity_creator.get_information("one")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        counter = 0
        message_counter = "🔃 Количество упоминаний в новостях: " + str(
            counter)
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_counter, parse_mode="Markdown")
    elif call.data == "university_1":
        message_about_university = univercity_creator.get_information("two")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        counter = 0
        message_counter = "🔃 Количество упоминаний в новостях: " + str(
            counter)
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_counter, parse_mode="Markdown")
    elif call.data == "university_2":
        message_about_university = univercity_creator.get_information("three")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        counter = 0
        message_counter = "🔃 Количество упоминаний в новостях: " + str(
            counter)
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_counter, parse_mode="Markdown")
    elif call.data == "university_3":
        message_about_university = univercity_creator.get_information("four")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        counter = 0
        message_counter = "🔃 Количество упоминаний в новостях: " + str(
            counter)
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_counter, parse_mode="Markdown")
    elif call.data == "university_4":
        message_about_university = univercity_creator.get_information("five")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        counter = 0
        message_counter = "🔃 Количество упоминаний в новостях: " + str(
            counter)
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_counter, parse_mode="Markdown")
    elif call.data == "university_5":
        message_about_university = univercity_creator.get_information("six")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        counter = 0
        message_counter = "🔃 Количество упоминаний в новостях: " + str(
            counter)
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_counter, parse_mode="Markdown")
    elif call.data == "university_6":
        message_about_university = univercity_creator.get_information("seven")
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_about_university, parse_mode="Markdown")
        counter = 0
        message_counter = "🔃 Количество упоминаний в новостях: " + str(
            counter)
        bot.send_message(chat_id=call.message.chat.id,
                         text=message_counter, parse_mode="Markdown")
    else:
        number_of_question = call.data
        answer, question = questions_creator.answers_print(number_of_question)
        message = "⁉️ *Ответ на вопрос №" + number_of_question + ":* " + question + "\n" + " " + "\n" + answer + \
                  "\n" + " " + "\n" + "🤤 Нажмите на другую кнопку, чтобы получить ответ на следующий вопрос."
        bot.send_message(chat_id=call.message.chat.id, text=message,
                         parse_mode="Markdown")


# Проверка времени:
def check_time():
    schedule.every().day.at("12:30").do(show_every_day_message_stat)
    schedule.every().day.at("12:00").do(show_every_day_message_news)
    schedule.every().day.at("15:00").do(show_every_day_message_news)
    schedule.every().day.at("19:41").do(show_every_day_message_news)
    schedule.every().day.at("22:00").do(show_every_day_message_news)
    while True:
        schedule.run_pending()
        time.sleep(1)


# Метод вывода ежедневного сообщения с обновленными новостями РТУ МИРЭА:
def show_every_day_message_news():
    news_creator.start_parse_pages(11)
    TEXT_MESSAGE = "📊 Новости \"*РТУ МИРЭА*\" обновились."
    for user in all_users:
        bot.send_message(user, TEXT_MESSAGE, parse_mode="Markdown")


# Метод вывода ежедневного сообщения с обновленной статисткой заболеваемости:
def show_every_day_message_stat():
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
