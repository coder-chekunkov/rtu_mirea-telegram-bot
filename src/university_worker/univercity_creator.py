import json
from src.log_worker import log_creator


# Данный скрипт собирает всю информацию о институтах РТУ МИРЭА:

# Метод отправки кнопок с выбором института:
def show_buttons_university(message, telebot, bot):
    # Создание лога:
    log_creator.make_log(message, "переход в \"Институты и кафедры\"")

    names = ["Институт информационных технологий",
             "Институт искусственного интеллекта",
             "Институт кибербезопасности и цифровых технологий",
             "Институт перспективных технологий и индустриального "
             "программирования", "Институт радиоэлектроники и информатики",
             "Институт технологий управления",
             "Институт тонких химических технологий им. М.В. Ломоносова"]
    buff_message = get_information("zero")
    keyboard_universities = telebot.types.InlineKeyboardMarkup()

    for i in range(len(names)):
        message_id = "university_" + str(i)
        buff_button = telebot.types.InlineKeyboardButton(text=names[i],
                                                         callback_data=message_id,
                                                         parse_mode="Markdown")
        keyboard_universities.add(buff_button)
    bot.send_message(message.from_user.id, buff_message,
                     reply_markup=keyboard_universities, parse_mode="Markdown")


# Метод получения информации о институте:
def get_information(tag):
    link = ""

    with open('university_worker/text_university_links.json', 'r',
              encoding='utf-8') as \
            file:
        texts = json.load(file)
    for text in texts:
        if text['tag'] == tag:
            link = text['link']

    file = open(link, 'r', encoding='utf-8')
    text = file.read()
    file.close()
    return text
