import json
import emoji


# Данный скрипт используется для получения всех вопросов/ответов.


# Функция для получения всех доступных вопросов:
def questions_print():
    all_Questions = emoji.emojize("⁉️") + " Часто задаваемые вопросы:" + "\n" + " " + "\n"

    with open('JSON_worker/question/questions.json', 'r', encoding='utf-8') as file:
        questions = json.load(file)
    for question in questions:
        all_Questions += "*" + (str(question['id']) + ".* " + question['question'] + "\n")

    all_Questions += " " + "\n"
    all_Questions += emoji.emojize(":keyboard:") + " Для того, чтобы получить ответ на вопрос введите его номер."
    return all_Questions


# Функция для получения ответа на вопрос с id "number":
def questions_read(number):
    with open('JSON_worker/question/questions.json', 'r', encoding='utf-8') as file:
        questions = json.load(file)
    for question in questions:
        if question['id'] == int(number):
            print(question['title'])
