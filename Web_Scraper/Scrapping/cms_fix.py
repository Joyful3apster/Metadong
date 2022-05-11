import collections

from bs4 import BeautifulSoup
import requests

source = requests.get("https://bger.li/147-III-218").text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('div', id='content')

def find_number(article):
    number = []
    for H in article.find_all('strong'):
        if H is not None and H.name != 'p':
            if H.get_text().replace('.', '').isnumeric():
                number.append(H.get_text())
    return number


def find_text(article):

    """Finde Erwägungen"""
    for H in article.find_all('h1'):
        if H.get_text() == 'Erwägungen':
            start = H

    """Liste mit allen Absatznummern"""
    Numbers = find_number(article)

    """Dict initialisieren"""
    Erwägungen = collections.defaultdict(list)

    """Element'Aus den Erwägungen:' überspringen"""
    start = start.find_next_sibling().find_next_sibling()

    """Das erste Element initialisieren"""
    Erwägungen[Numbers[0]].append(start.get_text()[len(Numbers[0]):])
    Numbers.pop(0)

    """Den nächsten Startpunkt finden"""
    start = start.find_next_sibling()

    """Algorithmus"""
    while True:
        if len(Numbers) == 1:
            for H in start.find_next_siblings():
                if start is not None and start.name != 'p':
                    break
                else:
                    Erwägungen[0].append(H.get_text())
            break
        if start.get_text()[0:len(Numbers[1])].replace('.', '').isnumeric():
            Erwägungen[Numbers[0]].append(start.get_text()[len(Numbers[0]):])
            Numbers.pop(0)
            start = start.find_next_sibling()
        else:
            Erwägungen[Numbers[0]].append(start.get_text()[len(Numbers[0]):])
            start = start.find_next_sibling()
    print(Erwägungen)
    return Erwägungen

find_text(article)
