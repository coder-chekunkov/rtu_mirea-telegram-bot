import telebot
import emoji
from telebot import types
from JSON_worker.question import questions_creator
from JSON_worker.fact import facts_creator
from JSON_worker.text import text_creator
from BS_worker.statistic.world import world_statistic_creator
from BS_worker.statistic.russia import russia_statistic_creator

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
        show_statistic(message)
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
        TEXT_ERROR_MESSAGE = text_creator.get_text("error")
        bot.send_message(message.from_user.id, TEXT_ERROR_MESSAGE)


# Метод отправки статистики по миру и России:
def show_statistic(message):
    buff_russia = "Россия " + emoji.emojize("🇷🇺")
    buff_world = "Мир " + emoji.emojize("🌎")
    buff_message = emoji.emojize("📊") + " Выберите статистику нужного региона:"

    keyboard_statistic = telebot.types.InlineKeyboardMarkup()
    button_russia = telebot.types.InlineKeyboardButton(text=buff_russia, callback_data="russia",
                                                       parse_mode="Markdown")
    button_world = telebot.types.InlineKeyboardButton(text=buff_world, callback_data="world",
                                                      parse_mode="Markdown")

    keyboard_statistic.add(button_russia, button_world)
    bot.send_message(message.from_user.id, buff_message, reply_markup=keyboard_statistic)


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
    show_answers(message)


# Метод вывода одного интересного факта:
def show_fact(message):
    TEXT_FACT = facts_creator.facts_print()
    bot.send_message(message.from_user.id, TEXT_FACT, parse_mode="Markdown")


# Метод вывода кнопок для получения ответа на определенный вопрос:
def show_answers(message):
    buff_message = emoji.emojize(":keyboard:") + " Для того, чтобы получить ответ на вопрос нажмите на нужную кнопку."
    keyboard_answers = telebot.types.InlineKeyboardMarkup()

    numbers = [1, 2, 3, 4, 5]
    for j in range(5):
        buff_button_one = telebot.types.InlineKeyboardButton(str(numbers[0]), callback_data=str(numbers[0]),
                                                             parse_mode="Markdown")
        buff_button_two = telebot.types.InlineKeyboardButton(str(numbers[1]), callback_data=str(numbers[1]),
                                                             parse_mode="Markdown")
        buff_button_three = telebot.types.InlineKeyboardButton(str(numbers[2]), callback_data=str(numbers[2]),
                                                               parse_mode="Markdown")
        buff_button_four = telebot.types.InlineKeyboardButton(str(numbers[3]), callback_data=str(numbers[3]),
                                                              parse_mode="Markdown")
        buff_button_five = telebot.types.InlineKeyboardButton(str(numbers[4]), callback_data=str(numbers[4]),
                                                              parse_mode="Markdown")
        keyboard_answers.row(buff_button_one, buff_button_two, buff_button_three, buff_button_four, buff_button_five)

        for i in range(5):
            numbers[i] += 5

    bot.send_message(message.from_user.id, buff_message, reply_markup=keyboard_answers)


# Обработчик нажатия на кнопку:
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data != "russia" and call.data != "world":
        number_of_question = call.data
        answer, question = questions_creator.answers_print(number_of_question)
        message = "⁉️ *Ответ на вопрос №" + number_of_question + ":* " + question + "\n" + " " + "\n" + answer + \
                  "\n" + " " + "\n" + "🤤 Нажмите на другую кнопку, чтобы получить ответ на следующий вопрос."
        bot.send_message(chat_id=call.message.chat.id, text=message, parse_mode="Markdown")
    else:
        if call.data == "russia":
            message_russia, message_region = russia_statistic_creator.get_statistic_russia()
            bot.send_message(chat_id=call.message.chat.id, text=message_russia, parse_mode="Markdown")
            bot.send_message(chat_id=call.message.chat.id, text=message_region, parse_mode="Markdown")
        if call.data == "world":
            message_world, message_countries = world_statistic_creator.get_statistic_world()
            bot.send_message(chat_id=call.message.chat.id, text=message_world, parse_mode="Markdown")
            bot.send_message(chat_id=call.message.chat.id, text=message_countries, parse_mode="Markdown")


# Непрерывное прослушивание пользователя:
bot.polling(none_stop=True, interval=0)
