import json


# Данный скрипт используется для подсчет количества слов в новостях.

# Метод подсчета количества слова в новостях:
def news_search(call, bot, word):
    buff_word = word
    word = word.lower()
    news_index = []
    counter = 0

    with open("news_worker/news_mirea/news_mirea_text.json", "r",
              encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            new = new.lower().strip()
            if word in new:
                news_index.append(counter)
            counter += 1

    if len(news_index) == 0:
        message = "По запросу \"*" + buff_word + "*\" ничего не найдено."
        bot.send_message(chat_id=call.message.chat.id, text=message,
                         parse_mode="Markdown", disable_web_page_preview=True)
    else:
        title_message = "По запросу \"*" + buff_word + "*\" найдено " + str(
            len(news_index)) + " новостей."
        news_output(call, bot, news_index)
        bot.send_message(chat_id=call.message.chat.id, text=title_message,
                         parse_mode="Markdown", disable_web_page_preview=True)


# Метод создания сообщения с информацией о слове:
def news_output(call, bot, news_index):
    title_message = ""
    i = 0
    buff_counter = 0
    counter_to_message = 0
    with open("news_worker/news_mirea/news_mirea_title.json", "r",
              encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            if len(news_index) <= 0:
                break
            if i == news_index[0]:
                counter_to_message += 1
                buff_counter += 1
                header = new['header']
                href = new['href']
                date = new['date']
                news_index.remove(i)
                title_message += "*" + str(buff_counter) + ".* [" + header \
                                 + "](" + href + "). \n*Дата новости:* " \
                                 + date + ". \n [------] \n"
                if counter_to_message == 15:
                    counter_to_message = 0
                    bot.send_message(chat_id=call.message.chat.id,
                                     text=title_message,
                                     parse_mode="Markdown",
                                     disable_web_page_preview=True)
                    title_message = ""
            i += 1
    if title_message != "":
        bot.send_message(chat_id=call.message.chat.id,
                         text=title_message,
                         parse_mode="Markdown",
                         disable_web_page_preview=True)
