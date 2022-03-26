import requests
from bs4 import BeautifulSoup
import json
import emoji

# Данный скрипт используется для получения статистики covid_19_worker по России.

# Регистрация ссылки от куда берется статистика:
URL = 'https://www.mirea.ru/covid/statistics/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


# Получение статистики по РФ с помощью BeautifulSoup:
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
                        'healed': tags[healed].text.strip()
                     }
                     }
        mirea_statistic.append(statistic)

        who_index+=3
        sicked+=3
        healed+=3

        with open("mirea_stat.json", 'w',
                  encoding='utf-8') as write_file:
            json.dump(mirea_statistic, write_file)

def show_mirea_stat():
    message = ''
    with open("mirea_stat.json", "r",
              encoding="utf-8") as file:
        statistic = json.load(file)
        for stat in statistic:
            who = stat["who"]
            sicked = stat["info"]["sicked"]
            healed = stat["info"]["healed"]
            message+= who + ' заболело: ' + sicked + '; выздоровело: ' + healed + '\n'

    return message

get_statistic_mirea()
print(show_mirea_stat())

