import requests
from bs4 import BeautifulSoup
import json
import emoji

# Данный скрипт используется для получения статистики COVID-19.

# Регистрация ссылки от куда берется статистика:
URL = 'https://news.google.com/covid19/map?hl=ru&gl=RU&ceid=RU%3Aru&mid=%2Fm%2F06bnz'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


def get_statistic_russia():
    russia_statistic = []

    all_sick = 0
    a_day = 1
    death = 4
    tags = soup.find_all('div', {'class': 'pcAJd'})
    values = soup.find_all('td', {'class': 'l3HOY'})

    for tag in tags:
        statistic = {'country': tag.text.replace(u'\xa0', ' '),
                     "info": {'all_sick': values[all_sick].text.replace(u'\xa0', ' '),
                              'sick_per_day': values[a_day].text.replace(u'\xa0', ' '),
                              'all_deaths': values[death].text.replace(u'\xa0', ' ')}}
        russia_statistic.append(statistic)
        all_sick += 5
        a_day += 5
        death += 5

    with open('russia_stat.json', 'w', encoding='utf-8') as write_file:
        json.dump(russia_statistic, write_file)

    message_russia, message_region = show_stat_russia()
    return message_russia, message_region


def show_stat_russia():
    message = emoji.emojize("🇷🇺") + " Статистика заболеваемости по *России*:" + "\n" + " " + "\n"
    message_region = emoji.emojize("🧭") + " ТОП-10 *областей и регионов* по заболеваемости:" + "\n" + " " + "\n"
    buff_counter = 1

    with open("russia_stat.json", "r", encoding='utf-8') as file:
        statistic = json.load(file)
        for stat in statistic:
            if stat["country"] == "Россия":
                all_sick = stat["info"]["all_sick"]
                sick_per_day = stat["info"]["sick_per_day"]
                all_deaths = stat["info"]["all_deaths"]
                message += "*Все случаи заболевания:* " + all_sick + "\n"
                message += "*Случае заболевания за день:* " + sick_per_day + "\n"
                message += "*Все случаи летального исхода:* " + all_deaths + "\n"

            if stat["country"] != "Россия" and stat["country"] != "Весь мир" and buff_counter <= 10:
                name_region = stat["country"]
                all_sick = stat["info"]["all_sick"]
                sick_per_day = stat["info"]["sick_per_day"]
                all_deaths = stat["info"]["all_deaths"]
                message_region += "*" + str(buff_counter) + ". " + name_region + ":* " + "\n"
                message_region += "Все случаи заболевания: " + all_sick + "; " + "\n"
                message_region += "Случае заболевания за день: " + sick_per_day + "; " + "\n"
                message_region += "Все случаи летального исхода: " + all_deaths + "; " + "\n"
                buff_counter += 1

    return message, message_region
