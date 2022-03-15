import requests
from bs4 import BeautifulSoup
import json

URL = 'https://news.google.com/topics/CAAqRggKIkBDQklTS2pvUVkyOTJhV1JmZEdWNGRGOXhkV1Z5ZVlJQkZRb0lMMjB2TURKcU56RVNDUzl0THpBeFkzQjVlU2dBUAE/sections/CAQqSggAKkYICiJAQ0JJU0tqb1FZMjkyYVdSZmRHVjRkRjl4ZFdWeWVZSUJGUW9JTDIwdk1ESnFOekVTQ1M5dEx6QXhZM0I1ZVNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru'

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')


def get_news():
    news_list = []
    headings = soup.find_all('a', {'class': 'DY5T1d RZIKme'}, limit=10)  # Заполнение списка названия стран парсингом

    for header in headings:
        # Создание словаря по образу
        slovar = {'header': header.text.replace(u'\xa0', ' '),
                  'href': ('https://news.google.com' + header.attrs.get("href").replace('.', '', 1))}
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
            header = new['header']
            href = new['href']
            message+= header + '\n' + href + '\n'
    return message






#news = json.load(open('JSON_worker/news/news.json'))

#for new in news:
#    print(f'{new["news"]}:   {new["href"]}\n')
