from bs4 import BeautifulSoup
import requests
import re

source = requests.get("https://bger.li/147-III-218").text
soup = BeautifulSoup(source,'lxml')

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

def get_text_Erw(H):
    abs = []
    number = []
    for sibling in H.find_next_siblings():
        if sibling.name is None or sibling.name != 'p':
            break
        else:
            Number = sibling.find('strong')
            if Number is not None:
                number.append(Number.get_text())
                abs.append(sibling.get_text())
    print(number)

""" Versuch: Die Absätze richtig in eine Dictionary zu speichern """
def list_sort(list):
    list.pop(0)
    example_dict = {}
    for abs in list:
        zahl = int(re.search(r'\d',abs).group())
        print(zahl)
get_text_Erw(find_Erwaegung(article))



