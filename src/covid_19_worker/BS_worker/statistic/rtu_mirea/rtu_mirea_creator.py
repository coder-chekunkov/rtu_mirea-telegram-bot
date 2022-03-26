import requests
from bs4 import BeautifulSoup
import json
import emoji

# Данный скрипт используется для получения статистики COVID-19 по РТУ МИРЭА.

# Регистрация ссылки от куда берется статистика:
URL = 'https://www.mirea.ru/covid/statistics/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


# Получение статистики по РТУ МИРЭА с помощью BeautifulSoup:
def get_statistic_mirea():
    mirea_statistic = []

    who_index = 0
    sicked = 1
    healed = 2

    table = soup.find('table')
    tags = table.find_all('td')

    for i in range(2):
        statistic = {'who': tags[who_index].text.strip(),
                     "info": {
                         'sicked': tags[sicked].text.strip(),
                         'healed': tags[healed].text.strip()}}
        mirea_statistic.append(statistic)

        who_index += 3
        sicked += 3
        healed += 3

        with open(
                "covid_19_worker/BS_worker/statistic/rtu_mirea/mirea_stat.json",
                'w', encoding='utf-8') as write_file:
            json.dump(mirea_statistic, write_file)

    message_title, message = show_mirea_stat()
    return message_title, message


# Создание сообщений со статистикой заболеваемости по РТУ МИРЭА:
def show_mirea_stat():
    message_title = emoji.emojize(
        "🏢") + "Заболеваемость COVID-19 в *РТУ МИРЭА*:"
    message = ''
    with open("covid_19_worker/BS_worker/statistic/rtu_mirea/mirea_stat.json", "r", encoding="utf-8") as file:
        statistic = json.load(file)
        for stat in statistic:
            who = stat["who"]
            sicked = stat["info"]["sicked"]
            healed = stat["info"]["healed"]
            if who == "Из числа обучающихся":
                message += "*Обучающихся* заболело: " + sicked + "; " \
                                                                 "выздоровело: " + healed + "; \n"
            else:
                message += "*Сотрудников* заболело: " + sicked + "; " \
                                                                 "выздоровело: " + healed + "; \n"

    return message_title, message
