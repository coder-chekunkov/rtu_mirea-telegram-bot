import requests
from bs4 import BeautifulSoup
import json

URL = 'https://www.interfax.ru/chronicle/novyj-koronavirus-v-kitae.html'

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')


def get_news():
    news_list = []
    headings = soup.find_all('a', {'tabindex': '3'},
                             limit=10)  # Заполнение списка названия стран парсингом

    for header in headings:
        slovar = {"header": header.attrs.get("title"),
                  "href": header.attrs.get("href")}
        news_list.append(slovar)

    with open('JSON_worker/news/news.json', 'w', encoding='utf-8') as write_file:
        json.dump(news_list, write_file)

    return (show_news())

def show_news():
    message = "Новости за последние 2 часа: \n"
    with open('JSON_worker/news/news.json', 'r', encoding='utf-8') as read_file:
        news = json.load(read_file)
        for new in news:
            if new['header'] == None:
                continue
            message+= new['header'] + '\n' + 'https://www.interfax.ru' + new['href'] + '\n'
    return message


print(get_news())


