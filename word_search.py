import json


def news_output(indeces):
    message = ''
    i = 0
    with open("news_mirea.json", "r",
              encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            if len(indeces) <= 0:
                break
            if i == indeces[0]:
                message+= f"{new['header']} ссылка: {new['href']}   дата: {new['date']} \n"
                indeces.remove(i)
            i+=1
    return message


def news_search(object):

    news_index = []
    k = 0

    with open("news_content.json", "r",
              encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            new = new.lower().strip()
            if object in new:
                news_index.append(k)
            k+=1

    print(news_output(news_index))

news_search(input())
