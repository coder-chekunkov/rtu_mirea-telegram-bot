import json
import random

import emoji


# Данный скрипт используется для получения фактов о COVID-19.


def facts_print():
    index = random.randint(1, 36)
    all_Facts = emoji.emojize("🤔") + " Интересный факт *№ " + str(index) + "*:" + "\n" + " " + "\n"

    with open("JSON_worker/fact/facts.json", "r", encoding='utf-8') as file:
        facts = json.load(file)
    for fact in facts:
        if fact['id'] == index:
            all_Facts += fact['fact'] + "\n"

    all_Facts += " " + "\n"
    all_Facts += emoji.emojize(":keyboard:") + " Введите \"/fact\", чтобы получить еще один интересный факт о COVID-19."
    return all_Facts
