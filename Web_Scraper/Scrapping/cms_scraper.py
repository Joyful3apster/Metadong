import collections

from bs4 import BeautifulSoup
import requests


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
    absatz = []
    number = []
    for sibling in H.find_next_siblings():
        if sibling.name is None or sibling.name != 'p':
            break
        else:
            Number = sibling.find('strong')
            if Number is not None:
                number.append(Number.get_text())
                absatz.append(sibling.get_text())
    return absatz

def get_number_Erw(H):

    number = []

    for sibling in H.find_next_siblings():
        if sibling.name is None or sibling.name != 'p':
            break
        else:
            Number = sibling.find('strong')
            if Number is not None:
                number.append(Number.get_text())
    return number



def Database_row(Absatz,number):
   for n in number:
        for abs in Absatz:
            Erwägungen = collections.defaultdict(list)
            tocheck = abs[0:len(n)].replace('.','')
            if(tocheck.isnumeric()):
                if(tocheck == n.replace('.','')):
                    pass
            if abs in Erwägungen.values():
                pass
            else:
                Erwägungen[str(n)].append(abs)
   print(Erwägungen)



H = find_Erwaegung(article)

Database_row(get_text_Erw(H),get_number_Erw(H))








                    #Fall_NR VARCHAR(1000),"
                   #ABS_NR VARCHAR(1000),"
                   #Textblock VARCHAR(1000), "
                   # Übereinstimmungen VARCHAR(1000)"""





