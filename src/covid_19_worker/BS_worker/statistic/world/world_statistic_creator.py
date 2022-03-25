import requests
from bs4 import BeautifulSoup
import json
import emoji

# Данный скрипт используется для получения статистики covid_19_worker по всему миру.

# Регистрация ссылки от куда берется статистика:
URL_minfin = 'https://index.minfin.com.ua/reference/coronavirus/geography/'

response = requests.get(URL_minfin)
soup = BeautifulSoup(response.content, 'html.parser')


# Получение статистики по миру с помощью BeautifulSoup:
def get_statistic_world():
    world_statistic = []

    all_sick = 0
    sick_a_day = 1
    all_deaths = 2
    death_a_day = 3
    all_healed = 4
    healed_a_day = 5


    table = soup.find('table')
    values_world = table.find_all('td', class_='bg-total')
    countries = table.find_all('a', limit=24)
    countries = countries[4:]
    values = table.find_all('td', class_='blank')

    general_stat = {'country': values_world[0].text.replace(u'\xa0', ' '),
                    "info": {
                        'all_sick': values_world[1].text.replace(u'\xa0', ' '),
                        'sick_a_day': values_world[2].text.replace(u'\xa0', ' '),
                        'all_deaths': values_world[3].text.replace(u'\xa0', ' '),
                        'death_a_day': values_world[4].text.replace(u'\xa0', ' '),
                        'all_healed': values_world[5].text.replace(u'\xa0', ' '),
                        'healed_a_day': values_world[6].text.replace(u'\xa0', ' ')
                    }
                    }
    world_statistic.append(general_stat)

    for country in countries:
        statistic = {'country': country.text,
                     "info": {
                         'all_sick': values[all_sick].text.replace(u'\xa0', ' '),
                         'sick_a_day': values[sick_a_day].text.replace(u'\xa0', ' '),
                         'all_deaths': values[all_deaths].text.replace(u'\xa0', ' '),
                         'death_a_day': values[death_a_day].text.replace(u'\xa0', ' '),
                         'all_healed': values[all_healed].text.replace(u'\xa0', ' '),
                         'healed_a_day': values[healed_a_day].text.replace(u'\xa0', ' ')
                            }
                     }
        print(statistic)

        world_statistic.append(statistic)

        all_sick+= 7
        sick_a_day+= 7
        all_deaths+= 7
        death_a_day+= 7
        all_healed+= 7
        healed_a_day+= 7

    with open("covid_19_worker/BS_worker/statistic/world/world_stat.json", 'w',
              encoding='utf-8') as write_file:
        json.dump(world_statistic, write_file)


# Создание сообщений со статистикой по странам и общей статистикой:
def show_stat_world():
    message = emoji.emojize(
        "🌎") + " Общая статистика заболеваемости по *Миру*: \n" + " \n"
    message_countries = emoji.emojize(
        "🧭") + " ТОП-10 *стран* по заболеваемости: \n" + " \n"
    buff_counter = 1

    with open("covid_19_worker/BS_worker/statistic/world/world_stat.json", "r",
              encoding="utf-8") as file:
        statistic = json.load(file)
        for stat in statistic:
            # if stat["country"] == "Всего":
            #     all_sick = stat["info"]["all_sick"]
            #     sick_a_day = stat["info"]["sick_a_day"]
            #     all_deaths = stat["info"]["all_deaths"]
            #     death_a_day = stat["info"]["death_a_day"]
            #     all_healed = stat["info"]["all_healed"]
            #     healed_a_day = stat["info"]["healed_a_day"]
            #     emoji_of_country = get_emoji_country(name_region)
            #     message += emoji_of_country + " *" + name_region + "*: " + "\n"
            #     message += "Все случаи заболевания: " + all_sick + "; " + "\n"
            #     message += "Случае заболевания за день: " + sick_a_day + "; " + "\n"
            #     message += "Все случаи летального исхода: " + all_deaths + "; " + "\n"
            #     message += "Cлучаи летального исхода за день: " + death_a_day + "; " + "\n"
            #     message += "Все случаи выздоровления: " + all_healed + "; " + "\n"
            #     message += "Случаи выздоровления за день: " + healed_a_day + "; " + "\n"

            if stat["country"] != "Весь мир" and buff_counter <= 10:
                name_region = stat["country"]
                all_sick = stat["info"]["all_sick"]
                sick_a_day = stat["info"]["sick_a_day"]
                all_deaths = stat["info"]["all_deaths"]
                death_a_day = stat["info"]["death_a_day"]
                all_healed = stat["info"]["all_healed"]
                healed_a_day = stat["info"]["healed_a_day"]
                emoji_of_country = get_emoji_country(name_region)
                message_countries += emoji_of_country + " *" + name_region + "*: " + "\n"
                message_countries += "Все случаи заболевания: " + all_sick + "; " + "\n"
                message_countries += "Случае заболевания за день: " + sick_a_day + "; " + "\n"
                message_countries += "Все случаи летального исхода: " + all_deaths + "; " + "\n"
                message_countries += "Cлучаи летального исхода за день: " + death_a_day + "; " + "\n"
                message_countries += "Все случаи выздоровления: " + all_healed + "; " + "\n"
                message_countries += "Случаи выздоровления за день: " + healed_a_day + "; " + "\n"
                buff_counter += 1

    return message, message_countries



#Создание флага страны по ее названию:
def get_emoji_country(name_region):
    if name_region == "США":
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


# def show_stat_world_every_day():
#     message = emoji.emojize("🌎") + " Статистика заболеваемости по *Миру*: \n"
#
#     with open("BS_worker/statistic/world/world_stat.json", "r",
#               encoding="utf-8") as file:
#         statistic = json.load(file)
#         for stat in statistic:
#             if stat["country"] == "Весь мир":
#                 all_sick = stat["info"]["all_sick"]
#                 sick_per_day = stat["info"]["sick_per_day"]
#                 message += "*Все случаи заболевания:* " + all_sick + "\n"
#                 message += "*Случае заболевания за день:* " + sick_per_day + "\n"
#     return message
