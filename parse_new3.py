import requests
from bs4 import BeautifulSoup
import json

URL = 'https://yandex.ru/news/rubric/koronavirus'

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')


def get_news():
    news_list = []
    headings = soup.find_all('a', {'class': 'mg-card__link'}, limit=10)  # Заполнение списка названия стран парсингом

    for header in headings:
        # Создание словаря по образу
        slovar = {'header': header.text.replace(u'\xa0', ' '),
                  'href': (header.attrs.get("href").replace('.', '', 1))}
        news_list.append(slovar)  # Добавление словаря в список ему подобных

    with open('JSON_worker/news/news.json', 'w', encoding='utf-8') as write_file:
        json.dump(news_list, write_file)

    message = show_news()
    return message


def show_news():
    message = "Новости за последние 2 часа: \n"
    with open('JSON_worker/news/news.json', 'r', encoding='utf-8') as read_file:
        news = json.load(read_file)
        for new in news:
            if new['header'] == None:
                continue
            message+= new['header'] + '\n' + new['href'] + '\n'
    return message


print(get_news())


