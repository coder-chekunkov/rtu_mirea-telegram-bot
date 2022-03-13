import requests
from bs4 import BeautifulSoup
import json

URL = 'https://news.google.com/topics/CAAqRggKIkBDQklTS2pvUVkyOTJhV1JmZEdWNGRGOXhkV1Z5ZVlJQkZRb0lMMjB2TURKcU56RVNDUzl0THpBeFkzQjVlU2dBUAE/sections/CAQqSggAKkYICiJAQ0JJU0tqb1FZMjkyYVdSZmRHVjRkRjl4ZFdWeWVZSUJGUW9JTDIwdk1ESnFOekVTQ1M5dEx6QXhZM0I1ZVNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru'

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')


def stat_create():
        slovar = {}
        slovar_spisok = []
        headings = soup.find_all('a', {'class': 'DY5T1d RZIKme'}, limit=10)    # Заполнение списка названия стран парсингом
        #hrefs = soup.find_all('td', {'class': 'l3HOY'})        # Заполнение списка значений свойств парсингом

        for header in headings:
            # Создание словаря по образу
            slovar = {'news': header.text.replace(u'\xa0', ' '), 'href': ('https://news.google.com'  + header.attrs.get("href").replace('.', '', 1))}
            slovar_spisok.append(slovar)                        # Добавление словаря в список ему подобных

        with open('JSON_worker/news/news.json', 'w', encoding='utf-8') as write_file:
            json.dump(slovar_spisok, write_file)


stat_create()

news = json.load(open('JSON_worker/news/news.json'))

for new in news:
    print(f'{new["news"]}:   {new["href"]}\n')


