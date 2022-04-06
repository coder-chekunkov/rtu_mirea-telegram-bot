import pandas as pd  # pip install pandas

df1 = pd.read_excel(r'C:\Users\tsink\Downloads\1.xlsx', sheet_name='Лист1')
df2 = pd.read_excel(r'C:\Users\tsink\Downloads\1.xlsx', sheet_name='Лист2')


def output(institute, kurs, group_name):
    if institute == 'III':
        iii = pd.read_excel(f"documents/shedule/III/{kurs}.xlsx", sheet_name='Лист1')

        index = group_finder(iii, group_name)

        parse_shedule(index, iii)

    if institute == 'IIT':
        iit = pd.read_excel(f"documents/shedule/IIT/{kurs}.xlsx", sheet_name='Лист1')

        index = group_finder(iit, group_name)

        parse_shedule(index, iit)

    if institute == 'IKB':
        ikb = pd.read_excel(f"documents/shedule/IKB/{kurs}.xlsx", sheet_name='Лист1')

        index = group_finder(ikb, group_name)

        parse_shedule(index, ikb)


    if institute == 'IPTIP':
        iptip = pd.read_excel(f"documents/shedule/IPTIP/{kurs}.xlsx", sheet_name='Лист1')

        index = group_finder(iptip, group_name)

        parse_shedule(index, iptip)

    if institute == 'IRI':
        iri = pd.read_excel(f"documents/shedule/IRI/{kurs}.xlsx", sheet_name='Лист1')

        index = group_finder(iri, group_name)

        parse_shedule(index, iri)

    if institute == 'ITHT':
        itht = pd.read_excel(f"documents/shedule/ITHT/{kurs}.xlsx", sheet_name='Лист1')

        index = group_finder(itht, group_name)

        parse_shedule(index, itht)

    if institute == 'ITU':
        itu = pd.read_excel(f"documents/shedule/ITU/{kurs}.xlsx", sheet_name='Лист1')

        index = group_finder(itu, group_name)

        parse_shedule(index, itu)


def parse_shedule(index, df):
    k = 0
    sch = 0
    for j in range(1, (len(df.columns)-7), 5):
        print(k)
        print(sch)
        if sch > 2:
            j+=5
            sch = 0
        for i in range(2, 14, 2):
            iter = 2
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i][j + 4]).replace('nan', '')} ({str(df.values[i][j + 5]).replace('nan', '')}) {str(df.values[i][j + 6]).replace('nan', '')} {str(df.values[i][j + 7]).replace('nan', '')}")
            iter += 1
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i + 1][j + 4]).replace('nan', '')} ({str(df.values[i + 1][j + 5]).replace('nan', '')}) {str(df.values[i + 1][j + 6]).replace('nan', '')} {str(df.values[i + 1][j + 7]).replace('nan', '')}")
        print('\n')
        for i in range(14, 26, 2):
            iter = 2
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i][j + 4]).replace('nan', '')} ({str(df.values[i][j + 5]).replace('nan', '')}) {str(df.values[i][j + 6]).replace('nan', '')} {str(df.values[i][j + 7]).replace('nan', '')}")
            iter += 1
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i + 1][j + 4]).replace('nan', '')} ({str(df.values[i + 1][j + 5]).replace('nan', '')}) {str(df.values[i + 1][j + 6]).replace('nan', '')} {str(df.values[i + 1][j + 7]).replace('nan', '')}")
        print('\n')
        for i in range(26, 38, 2):
            iter = 2
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i][j + 4]).replace('nan', '')} ({str(df.values[i][j + 5]).replace('nan', '')}) {str(df.values[i][j + 6]).replace('nan', '')} {str(df.values[i][j + 7]).replace('nan', '')}")
            iter += 1
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i + 1][j + 4]).replace('nan', '')} ({str(df.values[i + 1][j + 5]).replace('nan', '')}) {str(df.values[i + 1][j + 6]).replace('nan', '')} {str(df.values[i + 1][j + 7]).replace('nan', '')}")
        print('\n')
        for i in range(38, 50, 2):
            iter = 2
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i][j + 4]).replace('nan', '')} ({str(df.values[i][j + 5]).replace('nan', '')}) {str(df.values[i][j + 6]).replace('nan', '')} {str(df.values[i][j + 7]).replace('nan', '')}")
            iter += 1
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i + 1][j + 4]).replace('nan', '')} ({str(df.values[i + 1][j + 5]).replace('nan', '')}) {str(df.values[i + 1][j + 6]).replace('nan', '')} {str(df.values[i + 1][j + 7]).replace('nan', '')}")
        print('\n')
        for i in range(50, 62, 2):
            iter = 2
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i][j + 4]).replace('nan', '')} ({str(df.values[i][j + 5]).replace('nan', '')}) {str(df.values[i][j + 6]).replace('nan', '')} {str(df.values[i][j + 7]).replace('nan', '')}")
            iter += 1
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i + 1][j + 4]).replace('nan', '')} ({str(df.values[i + 1][j + 5]).replace('nan', '')}) {str(df.values[i + 1][j + 6]).replace('nan', '')} {str(df.values[i + 1][j + 7]).replace('nan', '')}")
        print('\n')
        for i in range(62, 74, 2):
            iter = 2
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i][j + 4]).replace('nan', '')} ({str(df.values[i][j + 5]).replace('nan', '')}) {str(df.values[i][j + 6]).replace('nan', '')} {str(df.values[i][j + 7]).replace('nan', '')}")
            iter += 1
            print(
                f"{str(df.values[i][1])}  [{str(df.values[i][2])} {str(df.values[i][3])}] {str(df.values[iter][4])} {str(df.values[i + 1][j + 4]).replace('nan', '')} ({str(df.values[i + 1][j + 5]).replace('nan', '')}) {str(df.values[i + 1][j + 6]).replace('nan', '')} {str(df.values[i + 1][j + 7]).replace('nan', '')}")
        print('\n\n')
        k += 1
        sch+=1


def group_finder(xl, group_name):
    groups = []
    for i in range(len(xl.columns)):
        if str(xl.values[0][i]).find('О-') != -1:
            groups.append(xl.values[0][i])

    for i in range(len(groups)):
        buff = groups[i]
        buff = buff[:10]
        groups[i] = buff

    index = 0
    k = 0
    for i in range(len(groups)):
        if (groups[i].lower() == group_name.lower()):
            index = k
        k += 1

    return index


output(input(), input(), input())
