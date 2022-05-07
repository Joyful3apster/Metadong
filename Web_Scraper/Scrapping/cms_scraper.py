import collections

from bs4 import BeautifulSoup
import requests

source = requests.get("https://bger.li/147-III-218").text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('div', id='content')

"""Findet Startpunkt um nextSibling für @find_Erwaegung zu nutzen"""


def find_Erwaegung(article):
    for H in article.find_all('h1'):
        if H.get_text() == 'Erwägungen':
            return H


""" Erstellt 2 Listen:
 1) abs = liste mit allen Textbausteinen (inkl. Absatznummer)
 2) number = liste mit allen Absatznummer 
    Grund: Nummer nötig zu jedem Absatz, um in der Datenbank richtig abzuspeichern"""


def get_text(start):
    Absatz = []
    for sibling in start.find_next_siblings():
        if sibling.name is None or sibling.name != 'p':
            break
        else:
            Absatz.append(sibling.get_text())

    Absatz.pop(0)
    print(Absatz)
    return Absatz


def get_number(start):
    number = []
    for sibling in start.find_next_siblings():
        if sibling.name is None or sibling.name != 'p':
            break
        else:
            Number = sibling.find('strong')
            if Number is not None:
                number.append(Number.get_text())
    return number


def Database_row(Absatz, number):
    print(number)
    Erwägungen = collections.defaultdict(list)
    temp = Absatz
    for n in number:
        for ab in Absatz:
            sliced = ab[0:len(n)]
            if not sliced:
                Erwägungen[n].append(0)
                Absatz.remove(ab)
            elif ab in Erwägungen.values():
                pass
            elif sliced.isnumeric():
                break
            else:
                Erwägungen[n].append("\n"+ab)
    print(Erwägungen)


H = find_Erwaegung(article)

Database_row(get_text(H), get_number(H))

# Fall_NR VARCHAR(1000),"
# ABS_NR VARCHAR(1000),"
# Textblock VARCHAR(1000), "
# Übereinstimmungen VARCHAR(1000)"""
print(len('3.3.2'))
