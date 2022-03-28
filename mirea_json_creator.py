import requests
from bs4 import BeautifulSoup
import json
from time import sleep



def parse_one(plots, url):
    response = requests.get(url)
    soup1 = BeautifulSoup(response.content, 'html.parser')
    plot = soup1.find('div', class_='news-item-text uk-margin-bottom')
    plots.append(plot.text.replace(('\n' and '\xa0' and '\r'), ''))


def get_mirea_news():

    headings = soup.find_all('div', {'class': 'uk-card uk-card-default'})
    for header in headings:
        title = header.find('a', class_='uk-link-reset')
        date = header.find('div', class_='uk-margin-small-bottom uk-text-small')
        news = {'header': title.text,
                'href': ('https://www.mirea.ru' + title.attrs.get("href")),
                'date': date.text.replace('\n', '').strip()
                }

        url = news['href']
        news_list.append(news)
        parse_one(plots, url)


    with open("news_mirea.json", "w",
                encoding="utf-8") as write_file:
        json.dump(news_list, write_file)

    with open("news_content.json", "w",
                encoding="utf-8") as write_file:
        json.dump(plots, write_file)




plots = []
news_list = []


for p in range(1, 2):
    URL = f"https://www.mirea.ru/news/?PAGEN_1={p}"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    get_mirea_news()








