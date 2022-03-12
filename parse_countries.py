import requests
from bs4 import BeautifulSoup
import json

URL = 'https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU%3Aru'

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')


def stat_create():
        slovar = {}
        slovar_spisok = []
        all = 0                         #
        a_day = 1                       # Индексы
        death = 4                       #
        countries = soup.find_all('div', {'class': 'pcAJd'})    # Заполнение списка названия стран парсингом
        values = soup.find_all('td', {'class': 'l3HOY'})        # Заполнение списка значений свойств парсингом

        for country in countries:
            # Создание словаря по образу
            slovar = {'country': country.text.replace(u'\xa0', ' '), "info": {'Все случаи заболевания': values[all].text.replace(u'\xa0', ' '), 'Случаи заболевания за день': values[a_day].text.replace(u'\xa0', ' '), 'Все случаи летального исхода': values[death].text.replace(u'\xa0', ' ')}}
            slovar_spisok.append(slovar)                        # Добавление словаря в список ему подобных
            all+=5
            a_day+=5
            death+=5

        with open('JSON_worker/stat/stat.json', 'w', encoding='utf-8') as write_file:
            json.dump(slovar_spisok, write_file)                # Загрузка списка словарей в JSON файл

# Функция с выводом статистики по стране
def stat_print():
    print('Введите название страны: ')
    x = input()
    for stat in statistic:
        if stat['country'] == x:
            print("1. Вся информация")
            print("2. Все случаи заболевания")
            print("3. Случаи заболевания за день")
            print("4. Вся случаи летального исхода")
            y = input()
            if y == '1':
                print(stat['info'])
            elif y =='2':
                print(stat['info']['Все случаи заболевания'])
            elif y =='3':
                print(stat['info']['Случаи заболевания за день'])
            elif y =='4':
                print(stat['info']['Вся случаи летального исхода'])

stat_create()
statistic = json.load(open('JSON_worker/stat/stat.json'))       # Открытие и расшифровка JSON файла

for stat in statistic:
    print(f'{stat}')
print('\n')

stat_print()

