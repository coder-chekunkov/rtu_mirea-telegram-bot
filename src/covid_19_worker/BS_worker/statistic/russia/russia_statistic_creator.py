import requests
from bs4 import BeautifulSoup
import json
import emoji

# Данный скрипт используется для получения статистики covid_19_worker по России.

# Регистрация ссылки от куда берется статистика:
URL = 'https://coronavirus-monitor.info/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


# Получение статистики по РФ с помощью BeautifulSoup:
def get_statistic_russia():
    russia_statistic = []

    sick = 4
    death = 5
    healed = 0

    tags = soup.find_all('div', {'class': 'flex-row first'}, limit=15)
    sick_and_death = soup.find_all('div', {'class': 'flex-row flex-row'})
    healed_ls = soup.find_all('div', {'class': 'flex-row flex-row cured'})
    tags = tags[1:]

    for tag in tags:
        statistic = {'country': tag.text.replace(u'\xa0', ' '),
                     "info": {
                         'all_sick': sick_and_death[sick].text[
                                     :sick_and_death[sick].text.find('+')],
                         'sick_a_day': sick_and_death[sick].text[
                                       sick_and_death[sick].text.find('+'):],
                         'all_deaths': sick_and_death[death].text[
                                       :sick_and_death[death].text.find('+')],
                         'death_a_day': sick_and_death[death].text[
                                        sick_and_death[death].text.find('+'):],
                         'all_healed': healed_ls[healed].text[
                                       :healed_ls[healed].text.find('+')],
                         'healed_a_day': healed_ls[healed].text[
                                         healed_ls[healed].text.find('+'):]
                     }
                     }
        russia_statistic.append(statistic)
        sick += 3
        death += 3
        healed += 1

    with open("covid_19_worker/BS_worker/statistic/russia/russia_stat.json",
              'w',
              encoding='utf-8') as write_file:
        json.dump(russia_statistic, write_file)


# Создание сообщений со статистикой по регионам и общей статистикой:
def show_stat_russia():
    message = emoji.emojize(
        "🇷🇺") + " Статистика заболеваемости по *России*:" + "\n" + " " + "\n"
    message_region = emoji.emojize(
        "🧭") + " ТОП-10 *областей и регионов* по заболеваемости:" + "\n" + " " + "\n"
    buff_counter = 1

    with open("covid_19_worker/BS_worker/statistic/russia/russia_stat.json",
              "r",
              encoding='utf-8') as file:
        statistic_r = json.load(file)
        for stat in statistic_r:
            if stat["country"] != "Россия" and stat["country"] != "Весь мир" \
                    and buff_counter <= 10:
                name_region = stat["country"]
                all_sick = stat["info"]["all_sick"]
                sick_per_day = stat["info"]["sick_a_day"]
                all_deaths = stat["info"]["all_deaths"]
                death_a_day = stat["info"]["death_a_day"]
                all_healed = stat["info"]["all_healed"]
                healed_a_day = stat["info"]["healed_a_day"]
                message_region += "*" + str(
                    buff_counter) + ". " + name_region + ":* " + "\n"
                message_region += "Все случаи заболевания: " + all_sick + "; " + "\n"
                message_region += "Случае заболевания за день: " + sick_per_day + "; " + "\n"
                message_region += "Все случаи летального исхода: " + all_deaths + "; " + "\n"
                message_region += "Случае летального исхода за день: " + death_a_day + "; " + "\n"
                message_region += "Все случаи выздоровления: " + all_healed + "; " + "\n"
                message_region += "Случае выздоровления за день: " + healed_a_day + "; " + "\n"
                buff_counter += 1

    with open("covid_19_worker/BS_worker/statistic/world/world_stat.json", "r",
              encoding="utf-8") as file:
        statistic_w = json.load(file)
        for stat in statistic_w:
            if stat["country"] == "Россия":
                name_region = stat["country"]
                all_sick = stat["info"]["all_sick"]
                sick_a_day = stat["info"]["sick_a_day"]
                all_deaths = stat["info"]["all_deaths"]
                death_a_day = stat["info"]["death_a_day"]
                all_healed = stat["info"]["all_healed"]
                healed_a_day = stat["info"]["healed_a_day"]
                message += " *" + name_region + "*: " + "\n"
                message += "Все случаи заболевания: " + all_sick + "; " + "\n"
                message += "Случае заболевания за день: " + sick_a_day + "; " + "\n"
                message += "Все случаи летального исхода: " + all_deaths + "; " + "\n"
                message += "Cлучаи летального исхода за день: " + death_a_day + "; " + "\n"
                message += "Все случаи выздоровления: " + all_healed + "; " + "\n"
                message += "Случаи выздоровления за день: " + healed_a_day + "; " + "\n"

    return message, message_region
