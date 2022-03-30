import json


# Данный скрипт используется для подсчет количества слов в новостях.

# Метод поиска количества упоминаний университета в новостях:
def university_search(university):
    news_index = []
    counter = 0

    with open("news_worker/news_mirea/news_mirea_text.json", "r",
              encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            new = new.lower().strip()

            if university == "CADT" and "кибербезопасности и цифровых технологий" in new:
                news_index.append(counter)
            if university == "IT" and "информационных технологий" in new:
                news_index.append(counter)
            if university == "II" and "искусственного интеллекта" in new:
                news_index.append(counter)
            if university == "ATIP" and "перспективных технологий и индустриального программирования" in new:
                news_index.append(counter)
            if university == "REI" and "радиоэлектроники и информатики" in new:
                news_index.append(counter)
            if university == "MT" and "технологий управления" in new:
                news_index.append(counter)
            if university == "FCTL" and "тонких химических технологий" in new:
                news_index.append(counter)
            counter += 1

    return news_index


# Метод создания сообщения со всеми новостями:
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
