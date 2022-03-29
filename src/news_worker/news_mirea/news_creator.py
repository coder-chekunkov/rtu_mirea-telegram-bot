import requests
from bs4 import BeautifulSoup
import json
import emoji


# Данный скрипт используется для создания и вывода новостей.

# Метод получения текста новостей:
def parse_news(texts, url):
    response = requests.get(url)
    soup1 = BeautifulSoup(response.content, 'html.parser')
    text = soup1.find('div', class_='news-item-text uk-margin-bottom')
    texts.append(text.text.replace(('\n' and '\xa0' and '\r'), ''))


# Метод получения заголовков новостей:
def get_mirea_news(soup):
    headings = soup.find_all('div', {'class': 'uk-card uk-card-default'})
    for header in headings:
        title = header.find('a', class_='uk-link-reset')
        date = header.find('div',
                           class_='uk-margin-small-bottom uk-text-small')
        news = {'header': title.text,
                'href': ('https://www.mirea.ru' + title.attrs.get("href")),
                'date': date.text.replace('\n', '').strip()
                }

        url = news['href']
        news_list.append(news)
        parse_news(texts, url)

    with open("news_worker/news_mirea/news_mirea_title.json", "w",
              encoding="utf-8") as write_file:
        json.dump(news_list, write_file)

    with open("news_worker/news_mirea/news_mirea_text.json", "w",
              encoding="utf-8") as write_file:
        json.dump(texts, write_file)


# Парсинг нужных страниц с новостного портала:
def start_parse_pages(dates):
    for p in range(1, dates):
        URL = f"https://www.mirea.ru/news/?PAGEN_1={p}"
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        get_mirea_news(soup)


# Метод отправки сообщений с новостями:
def show_mirea_news(call, bot, count):
    message = emoji.emojize(
        "📑") + " Последние *" + str(count) + "* новостей с сайта *РТУ МИРЭА*:"
    bot.send_message(chat_id=call.message.chat.id,
                     text=message, parse_mode="Markdown")

    title_message = ""
    buff_counter = 0
    counter_to_message = 0

    with open("news_worker/news_mirea/news_mirea_title.json", "r",
              encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            if buff_counter < count:
                buff_counter += 1
                if new['header'] is not None:
                    counter_to_message += 1
                    header = new['header']
                    href = new['href']
                    date = new['date']
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
            else:
                if title_message != "":
                    bot.send_message(chat_id=call.message.chat.id,
                                     text=title_message,
                                     parse_mode="Markdown",
                                     disable_web_page_preview=True)
                break


texts = []
news_list = []
