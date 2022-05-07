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


def find_number(aritcle):
    number = []
    for H in article.find_all('strong'):
        if H is not None and H.name != 'p':
            if H.get_text().replace('.', '').isnumeric():
                number.append(H)
    return number


def find_text(start):
    Absatz = []
    for sibling in start.find_next_siblings():
        if sibling.name is None or sibling.name != 'p':
            break
        else:
            Absatz.append(sibling.get_text())

    return Absatz


""" Erstellt 2 Listen:
 1) abs = liste mit allen Textbausteinen (inkl. Absatznummer)
 2) number = liste mit allen Absatznummer 
    Grund: Nummer nötig zu jedem Absatz, um in der Datenbank richtig abzuspeichern"""


def dict_generator(article):
    Erwägungen = collections.defaultdict(list)
    for H in article.find_all('strong'):
        if H is not None and H.name != 'p':
            if H.get_text().replace('.', '').isnumeric():
                Erwägungen[H.get_text()]
                for sibling in H.find_next_siblings():
                    Erwägungen[H.get_text()].append(sibling.get_text())
                    if sibling.next_element.name != 'strong':
                        Erwägungen[H.get_text()].append(sibling.next_element.get_text())
                    else:
                        break
    print(Erwägungen)


dict_generator(article)

"""  for sibling in start.find_next_siblings():
        if sibling.name is None or sibling.name != 'p':
            break
        else:
            Number = sibling.find('strong')
            number.append(Number)
    print(number)
    counter = 0
    for next_ in number:
        Erwägungen[next_]
        for sibling in next_.find_next_siblings():
            if sibling.name is None or sibling.name != 'p':
                break
            if sibling is number[counter + 1]:
                counter += 1
                break
            else:
                Erwägungen[Number.get_text()].append(next_.text)
    print(Erwägungen)"""

find_number(article)
