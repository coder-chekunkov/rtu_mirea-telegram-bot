import requests
from bs4 import BeautifulSoup
import json
import emoji

# Данный скрипт используется для получения новостей covid_19_worker по России (rbk.com).


# Регистрация ссылки от куда BS получает новости:

URL = 'https://www.rbc.ru/story/5e2881539a794724ab627caa'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


# Получение заголовков и ссылок на новости:
def get_google_news():
    news_list = []
    headings = soup.find_all('a', {'class': 'item__link'}, limit=10)

    for header in headings:
        news = {'header': header.text.strip(),
                'href': (header.attrs.get("href"))}
        news_list.append(news)

    with open("covid_19_worker/BS_worker/news/rbk/news_google.json", "w",
              encoding="utf-8") as write_file:
        json.dump(news_list, write_file)

    message = show_google_news()
    return message


# Создание сообщения со всеми новостями:
def show_google_news():
    message = emoji.emojize(
        "📑") + " Самые актуальные новости с сайта \"rbk.com\": \n \n"
    buff_counter = 1

    with open("covid_19_worker/BS_worker/news/rbk/news_google.json", "r",
              encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            header = new['header']
            href = new['href']
            message += '*' + str(
                buff_counter) + ".* [" + header + "]" + "(" + href + ").\n \n"
            buff_counter += 1
    return message
