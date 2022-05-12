import collections

from bs4 import BeautifulSoup
import requests

source = requests.get("https://bger.li/138-II-440").text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('div', id='content')

"""Finde Erwägungen"""


def find_start(article):
    for H in article.find_all('h1'):
        if H.get_text() == 'Erwägungen':
            return H


def find_number(article):
    number = []
    for H in article.find_all('strong'):
        if H is not None and H.name != 'p':
            if H.get_text().replace('.', '').isnumeric():
                number.append(H.get_text())
    print(number)
    return number


def find_text(start, article):

    """Liste mit allen Absatznummern"""
    Numbers = find_number(article)

    """Dict initialisieren"""
    Erwägungen = collections.defaultdict(list)

    """Element'Aus den Erwägungen:' überspringen"""
    start = start.find_next_sibling().find_next_sibling()

    """Algorithmus"""
    while True:

        """Handling wenn Numbers genau ein Element noch hat"""
        if len(Numbers) == 1:
            for H in start.find_next_siblings():
                if start is not None and start.name != 'p':
                    break
                else:
                    Erwägungen[0].append(H.get_text())
            break

        """Vorkalkulationen"""
        temp = start.find_next_sibling()
        num = Numbers[0]
        nextnum = Numbers[1]
        Test_next_line_numeric = temp.get_text()[0:len(nextnum)].replace('.', '').isnumeric()
        Test_next_line_same = temp.get_text()[0:len(nextnum)] is not start.get_text()[0:len(num)]
        Test_line_to_cut = start.get_text()[0:len(num)].replace('.', '').isnumeric()
        to_save_cut = start.get_text()[len(num):]
        to_save = start.get_text()
        """"""""""""""""""""""""""""""

        if Test_next_line_numeric and Test_next_line_same:
            if Test_line_to_cut:
                Erwägungen[num].append(to_save_cut)
            else:
                Erwägungen[num].append(to_save)
            Numbers.pop(0)
            start = start.find_next_sibling()
        else:
            Erwägungen[num].append(to_save)
            start = start.find_next_sibling()
    print(Erwägungen)
    return Erwägungen


find_text(find_start(article), article)
