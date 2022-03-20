import requests
from bs4 import BeautifulSoup
import json
import emoji

# Данный скрипт используется для получения новостей COVID-19 по России.


# Регистрация ссылки от куда BS получает новости:
URL = 'https://news.google.com/topics/CAAqRggKIkBDQklTS2pvUVkyOTJhV1JmZEdWNGRGOXhkV1Z5ZVlJQkZRb0lMMjB2TURKcU56RVNDUzl0THpBeFkzQjVlU2dBUAE/sections/CAQqSggAKkYICiJAQ0JJU0tqb1FZMjkyYVdSZmRHVjRkRjl4ZFdWeWVZSUJGUW9JTDIwdk1ESnFOekVTQ1M5dEx6QXhZM0I1ZVNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


# Получение заголовков и ссылок на новости:
def get_google_news():
    news_list = []
    headings = soup.find_all('a', {'class': 'DY5T1d RZIKme'}, limit=10)

    for header in headings:
        news = {'header': header.text.replace(u'\xa0', ' '),
                'href': ('https://news.google.com' + header.attrs.get("href").replace('.', '', 1))}
        news_list.append(news)

    with open("BS_worker/news/news_google.json", 'w', encoding='utf-8') as write_file:
        json.dump(news_list, write_file)

    message = show_google_news()
    return message


# Создание сообщения со всеми новостями:
def show_google_news():
    message = emoji.emojize("📑") + " Самые актуальные новости с сайта \"google.com\": \n \n"
    buff_counter = 1

    with open("BS_worker/news/news_google.json", 'r', encoding='utf-8') as read_file:
        news = json.load(read_file)
        for new in news:
            header = new['header']
            href = new['href']
            message += '*' + str(buff_counter) + ".* [" + header + "]" + "(" + href + ").\n \n"
            buff_counter += 1
    return message
