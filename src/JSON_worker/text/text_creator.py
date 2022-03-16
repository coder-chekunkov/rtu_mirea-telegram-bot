import json


# Данный скрипт используется для получения текста из документов Markdown.

def get_text(tag):
    link = ""

    with open('src/JSON_worker/text/texts.json', 'r', encoding='utf-8') as file:
        texts = json.load(file)
    for text in texts:
        if text['tag'] == tag:
            link = text['link']

    file = open(link, 'r', encoding='utf-8')
    text = file.read()
    file.close()
    return text
