# # Метод вывода сообщения с дальнейшими действиями:
# def show_answer(message):
#     # Текст для ввода "Да":
#     TEXT_BUTTON_YES = "Да " + emoji.emojize("✅")
#
#     # Текст для ввода "Нет":
#     TEXT_BUTTON_NO = "Нет " + emoji.emojize("❌")
#
#     isFoundTag, tag = tags_cheking.tag_finder(message.text)
#     if isFoundTag:
#         # Запись конечного вопроса пользователю, в зависимости от тега:
#         buff_message = ""
#         if tag == "статистика":
#             buff_message = emoji.emojize(":bar_chart:") + " Вы хотите посмотреть статистику?"
#             button_YES = telebot.types.InlineKeyboardButton(TEXT_BUTTON_YES, callback_data='yes_stat',
#                                                             parse_mode="Markdown")
#         elif tag == "новости":
#             buff_message = emoji.emojize(":bookmark_tabs:") + " Вы хотите посмотреть актуальные новости?"
#             button_YES = telebot.types.InlineKeyboardButton(TEXT_BUTTON_YES, callback_data='yes_news',
#                                                             parse_mode="Markdown")
#         elif tag == "симптомы":
#             buff_message = emoji.emojize("🤕") + " Вы хотите узнать о симптомах COVID-19?"
#             button_YES = telebot.types.InlineKeyboardButton(TEXT_BUTTON_YES, callback_data='yes_symptoms',
#                                                             parse_mode="Markdown")
#         elif tag == "профилактика":
#             buff_message = emoji.emojize("😷") + " Вы хотите узнать о профилактики?"
#             button_YES = telebot.types.InlineKeyboardButton(TEXT_BUTTON_YES, callback_data='yes_prevention',
#                                                             parse_mode="Markdown")
#         elif tag == "вопросы":
#             buff_message = emoji.emojize("⁉️") + " Показать часто задаваемые вопросы?"
#             button_YES = telebot.types.InlineKeyboardButton(TEXT_BUTTON_YES, callback_data='yes_questions',
#                                                             parse_mode="Markdown")
#         elif tag == "факт":
#             buff_message = emoji.emojize("🤔") + " Показать интересный факт?"
#             button_YES = telebot.types.InlineKeyboardButton(TEXT_BUTTON_YES, callback_data='yes_fact',
#                                                             parse_mode="Markdown")
#         elif tag == "разработчики":
#             buff_message = emoji.emojize("🤔") + " Показать контакты разработчиков?"
#             button_YES = telebot.types.InlineKeyboardButton(TEXT_BUTTON_YES, callback_data='yes_develop',
#                                                             parse_mode="Markdown")
#
#         # Вывод вопроса и двух кнопок "да" или "нет":
#         keyboard_YES_NO = telebot.types.InlineKeyboardMarkup()
#         button_NO = telebot.types.InlineKeyboardButton(TEXT_BUTTON_NO, callback_data='no', parse_mode="Markdown")
#         keyboard_YES_NO.row(button_YES, button_NO)
#         bot.send_message(message.from_user.id, buff_message, reply_markup=keyboard_YES_NO)
#     else:
#         TEXT_ERROR_MESSAGE = text_creator.get_text("error")
#         bot.send_message(message.from_user.id, TEXT_ERROR_MESSAGE)
#
#
# @bot.message_handler(content_types=['text'])
# @bot.callback_query_handler(func=lambda call: True)
# def callback_data(call):
#     if call.data == "no":
#         TEXT_ERROR_MESSAGE = text_creator.get_text("error")
#         bot.send_message(chat_id=call.message.chat.id, text=TEXT_ERROR_MESSAGE)
#     elif call.data == "yes_stat":
#         TEXT_STATISTIC_MESSAGE = emoji.emojize(
#             "📊") + " Для того чтобы посмотреть статистику заболеваемости введите: \"/stat\""
#         bot.send_message(chat_id=call.message.chat.id, text=TEXT_STATISTIC_MESSAGE, parse_mode="Markdown")
#     elif call.data == "yes_news":
#         TEXT_NEWS_MESSAGE = emoji.emojize(
#             "📑") + " Для того чтобы посмотреть новости введите: \"/news\""
#         bot.send_message(chat_id=call.message.chat.id, text=TEXT_NEWS_MESSAGE, parse_mode="Markdown")
#     elif call.data == "yes_symptoms":
#         TEXT_SYMPTOMS_MESSAGE = emoji.emojize(
#             "🤕") + " Для того чтобы симптомы COVID-19 введите: \"/symptoms\""
#         bot.send_message(chat_id=call.message.chat.id, text=TEXT_SYMPTOMS_MESSAGE, parse_mode="Markdown")
#     elif call.data == "yes_prevention":
#         TEXT_PREVENTION_MESSAGE = emoji.emojize(
#             "😷") + " Для того чтобы профилактику COVID-19 введите: \"/prevention\""
#         bot.send_message(chat_id=call.message.chat.id, text=TEXT_PREVENTION_MESSAGE, parse_mode="Markdown")
#     elif call.data == "yes_questions":
#         TEXT_QUESTIONS_MESSAGE = emoji.emojize(
#             "⁉️") + " Для того чтобы посмотреть на часто задаваемые вопросы введите: \"/questions\""
#         bot.send_message(chat_id=call.message.chat.id, text=TEXT_QUESTIONS_MESSAGE, parse_mode="Markdown")
#     elif call.data == "yes_fact":
#         TEXT_FACT_MESSAGE = emoji.emojize(
#             "🤔") + " Для того чтобы получить интересный факт введите: \"/fact\""
#         bot.send_message(chat_id=call.message.chat.id, text=TEXT_FACT_MESSAGE, parse_mode="Markdown")
#     elif call.data == "yes_develop":
#         TEXT_DEVELOP_MESSAGE = emoji.emojize(
#             "🧑‍💻") + " Для того чтобы связаться с разработчиками введите: \"/develop\""
#         bot.send_message(chat_id=call.message.chat.id, text=TEXT_DEVELOP_MESSAGE, parse_mode="Markdown")
#
