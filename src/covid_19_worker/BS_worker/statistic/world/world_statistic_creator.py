import requests
from bs4 import BeautifulSoup
import json
import emoji

# Данный скрипт используется для получения статистики covid_19_worker по всему миру.

# Регистрация ссылки от куда берется статистика:
URL = 'https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU%3Aru'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


# Получение статистики по миру с помощью BeautifulSoup:
def get_statistic_world():
    world_statistic = []

    all_sick = 0
    a_day = 1
    death = 4
    tags = soup.find_all('div', {'class': 'pcAJd'})
    values = soup.find_all('td', {'class': 'l3HOY'})

    for tag in tags:
        statistic = {'country': tag.text.replace(u'\xa0', ' '),
                     "info": {
                         'all_sick': values[all_sick].text.replace(u'\xa0',
                                                                   ' '),
                         'sick_per_day': values[a_day].text.replace(u'\xa0',
                                                                    ' '),
                         'all_deaths': values[death].text.replace(u'\xa0',
                                                                  ' ')}}
        world_statistic.append(statistic)
        all_sick += 5
        a_day += 5
        death += 5

    with open("BS_worker/statistic/world/world_stat.json", 'w',
              encoding='utf-8') as write_file:
        json.dump(world_statistic, write_file)


# Создание сообщений со статистикой по странам и общей статистикой:
def show_stat_world():
    message = emoji.emojize(
        "🌎") + " Общая статистика заболеваемости по *Миру*: \n" + " \n"
    message_countries = emoji.emojize(
        "🧭") + " ТОП-10 *стран* по заболеваемости: \n" + " \n"
    buff_counter = 1

    with open("BS_worker/statistic/world/world_stat.json", "r",
              encoding="utf-8") as file:
        statistic = json.load(file)
        for stat in statistic:
            if stat["country"] == "Весь мир":
                all_sick = stat["info"]["all_sick"]
                sick_per_day = stat["info"]["sick_per_day"]
                all_deaths = stat["info"]["all_deaths"]
                message += "*Все случаи заболевания:* " + all_sick + "\n"
                message += "*Случае заболевания за день:* " + sick_per_day + "\n"
                message += "*Все случаи летального исхода:* " + all_deaths + "\n"

            if stat["country"] != "Весь мир" and buff_counter <= 10:
                name_region = stat["country"]
                all_sick = stat["info"]["all_sick"]
                sick_per_day = stat["info"]["sick_per_day"]
                all_deaths = stat["info"]["all_deaths"]
                emoji_of_country = get_emoji_country(name_region)
                message_countries += emoji_of_country + " *" + name_region + "*: " + "\n"
                message_countries += "Все случаи заболевания: " + all_sick + "; " + "\n"
                message_countries += "Случае заболевания за день: " + sick_per_day + "; " + "\n"
                message_countries += "Все случаи летального исхода: " + all_deaths + "; " + "\n"

                buff_counter += 1

    return message, message_countries


# Создание флага страны по ее названию:
def get_emoji_country(name_region):
    if name_region == "Соединенные Штаты Америки":
        return "🇺🇸"
    elif name_region == "Индия":
        return "🇮🇳"
    elif name_region == "Бразилия":
        return "🇧🇷"
    elif name_region == "Франция":
        return "🇫🇷"
    elif name_region == "Великобритания":
        return "🇬🇧"
    elif name_region == "Германия":
        return "🇩🇪"
    elif name_region == "Россия":
        return "🇷🇺"
    elif name_region == "Турция":
        return "🇹🇷"
    elif name_region == "Италия":
        return "🇮🇹"
    elif name_region == "Испания":
        return "🇪🇸"
    elif name_region == "Аргентина":
        return "🇦🇷"
    elif name_region == "Нидерланды":
        return "🇳🇱"
    elif name_region == "Южная Корея":
        return "🇰🇷"
    else:
        return "🌐"


def show_stat_world_every_day():
    message = emoji.emojize("🌎") + " Статистика заболеваемости по *Миру*: \n"

    with open("BS_worker/statistic/world/world_stat.json", "r",
              encoding="utf-8") as file:
        statistic = json.load(file)
        for stat in statistic:
            if stat["country"] == "Весь мир":
                all_sick = stat["info"]["all_sick"]
                sick_per_day = stat["info"]["sick_per_day"]
                message += "*Все случаи заболевания:* " + all_sick + "\n"
                message += "*Случае заболевания за день:* " + sick_per_day + "\n"
    return message
