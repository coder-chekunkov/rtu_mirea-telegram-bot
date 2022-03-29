import requests
from bs4 import BeautifulSoup
import json
import emoji

# Данный скрипт используется для получения новостей covid_19_worker по России (interfax.ru).

# Регистрация ссылки от куда BS получает новости:

URL = 'https://www.interfax.ru/chronicle/novyj-koronavirus-v-kitae.html'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


# Получение заголовков и ссылок на новости:
def get_interfax_news():
    news_list = []
    headings = soup.find_all('a', {'tabindex': '3'}, limit=10)

    for header in headings:
        news = {"header": header.attrs.get("title"),
                "href": 'https://interfax.ru' + header.attrs.get("href")}
        news_list.append(news)

    with open("covid_19_worker/BS_worker/news/interfax/news_interfax.json",
              "w", encoding="utf-8") as write_file:
        json.dump(news_list, write_file)

    message = show_interfax_news()
    return message


# Создание сообщения со всеми новостями:
def show_interfax_news():
    message = emoji.emojize(
        "📑") + " Самые актуальные новости с сайта \"interfax.ru\": \n \n"
    buff_counter = 1

    with open("covid_19_worker/BS_worker/news/interfax/news_interfax.json",
              "r", encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            if new['header'] is not None:
                header = new['header']
                href = new['href']
                message += '*' + str(
                    buff_counter) + ".* [" + header + "]" + "(" + href + \
                           ").\n [------] \n"
                buff_counter += 1
    return message
