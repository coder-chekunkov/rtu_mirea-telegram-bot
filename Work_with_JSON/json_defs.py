import json


def questions_print():
    stroka = ''
    with open('Work_with_JSON/faq.json', 'r', encoding='utf-8') as file:
        questions = json.load(file)
    for question in questions:
        stroka += (str(question['id']) + '. ' + question['question'] + '\n')
    return stroka



def questions_read(number):
    with open('Work_with_JSON/faq.json', 'r', encoding='utf-8') as file:
        questions = json.load(file)
    for question in questions:
        if question['id'] == int(number):
            print(question['title'])
