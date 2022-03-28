import json


def news_output(indeces):
    message = ''
    i = 0
    print(indeces)
    with open("news_mirea.json", "r",
              encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            if len(indeces) <= 0:
                break
            if i == indeces[0]:
                message+= f"{new['header']} ссылка: {new['href']}   дата: {new['date']} \n"
                indeces.remove(i)
                print(indeces)
            i+=1
    return message




def news_search(object):

    k = 0
    k_ITU = 0
    k_IKB = 0
    k_ITHT = 0
    k_IPTIP = 0
    k_IIT = 0
    k_IRI = 0
    k_III = 0
    ITU = []
    IKB = []
    ITHT = []
    IPTIP = []
    IIT = []
    IRI = []
    III = []

    with open("news_content.json", "r",
              encoding="utf-8") as read_file:
        news = json.load(read_file)
        for new in news:
            new = new.lower().strip()
            if object == 'ИТУ':
                if ('технологий управления') in new:
                    k_ITU+=1
                    ITU.append(k)
            elif object == 'ИКБ':
                if ('кибербезопасности и цифровых технологий') in new:
                    k_IKB+=1
                    IKB.append(k)
            elif object == 'ИТХТ':
                if ('тонких химических технологий') in new:
                    k_ITHT+=1
                    ITHT.append(k)
            elif object == 'ИПТИП':
                if ('перспективных технологий и индустриального программирования') in new:
                    k_IPTIP+=1
                    IPTIP.append(k)
            elif object == 'ИИТ':
                if ('информационных технологий') in new:
                    k_IIT+=1
                    IIT.append(k)
            elif object == 'ИРИ':
                if ('радиоэлектроники и информатики') in new:
                    k_IRI+=1
                    IRI.append(k)
            elif object == 'ИИИ':
                if ('искусственного интеллекта') in new:
                    k_III+=1
                    III.append(k)

            k+=1

    print('Сколько раз институт технологий управления упоминался в новостях: ' + str(k_ITU) + '\n')
    print('Сколько раз институт кибербезопасности и цифровых технологий упоминался в новостях: ' + str(k_IKB) + '\n')
    print('Сколько раз институт тонких химических технологий упоминался в новостях: ' + str(k_ITHT) + '\n')
    print('Сколько раз институт перспективных технологий и индустриального программирования упоминался в новостях: ' + str(k_IPTIP) + '\n')
    print('Сколько раз институт информационных технологий упоминался в новостях: ' + str(k_IIT) + '\n')
    print('Сколько раз институт радиоэлектроники и информатики упоминался в новостях: ' + str(k_IRI) + '\n')
    print('Сколько раз институт искусственного интеллекта упоминался в новостях: ' + str(k_III) + '\n')

    print(news_output(ITHT))


news_search(input())

