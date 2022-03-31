from src.log_worker import log_creator


# Данный скрипт используется для отправки возможного количества новостей:

# Метод отправки клавиатуры:
def show_dates_button(message, telebot, bot):
    # Создание лога:
    log_creator.make_log(message, "переход в \"Новости\"")

    keyboard_dates = telebot.types.InlineKeyboardMarkup()

    last_10_news = "Последние 10 новостей 📆"
    button_last_10_news = telebot.types.InlineKeyboardButton(
        text=last_10_news, callback_data="last_10_news",
        parse_mode="Markdown")
    keyboard_dates.add(button_last_10_news)

    last_20_news = "Последние 20 новостей 📆"
    button_last_20_news = telebot.types.InlineKeyboardButton(
        text=last_20_news, callback_data="last_20_news",
        parse_mode="Markdown")
    keyboard_dates.add(button_last_20_news)

    last_30_news = "Последние 30 новостей 📆"
    button_last_30_news = telebot.types.InlineKeyboardButton(
        text=last_30_news, callback_data="last_30_news",
        parse_mode="Markdown")
    keyboard_dates.add(button_last_30_news)

    last_40_news = "Последние 40 новостей 📆"
    button_last_40_news = telebot.types.InlineKeyboardButton(
        text=last_40_news, callback_data="last_40_news",
        parse_mode="Markdown")
    keyboard_dates.add(button_last_40_news)

    update_news = "Обновить новости 🔃"
    button_update_news = telebot.types.InlineKeyboardButton(
        text=update_news, callback_data="update_news",
        parse_mode="Markdown")
    keyboard_dates.add(button_update_news)

    bot.send_message(message.from_user.id,
                     "📆 Выберите количество новостей *РТУ МИРЭА*:",
                     reply_markup=keyboard_dates, parse_mode="Markdown")
