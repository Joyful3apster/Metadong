import collections

from bs4 import BeautifulSoup
import requests

source = requests.get("https://bger.li/147-II-209").text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('div', id='content')


def find_start(html):
    """@:return h1 tag mit Inhalt Erwägung im Leitentscheid als Ankerpunkt"""

    for H in html.find_all('h1'):
        if H.get_text() == 'Erwägungen':
            return H


def find_number(html):
    """Unter gegeben html "Ankerpunkt" gibt es nummerische Absätze
    mit tag <strong>.
    @:parameter html Ankerpunkt zum durch iterieren
    @:return Diese Nummer werden als Liste zurückgegeben """

    number = []
    for H in html.find_all('strong'):
        if H is not None and H.name != 'p':
            if H.get_text().replace('.', '').isnumeric():
                number.append(H.get_text())
    print(number)
    return number


def find_text(html):
    """Erstellt ein @:rtype dict (default list)
    @:return: Erstellt dict mit allen Absätzen (values) zum passender Nummer (keys)
    @:parameter:html: Html Datei"""

    Numbers = find_number(html)
    start = find_start(html)

    """Dict initialisieren"""
    Erwaegungen = collections.defaultdict(list)

    """Element 'Aus den Erwägungen:' überspringen"""
    start = start.find_next_sibling().find_next_sibling()

    """Algorithmus"""
    while True:

        """Handling wenn Numbers genau ein Element noch hat"""
        if len(Numbers) == 1:
            Erwaegungen[0].append(start.get_text())
            start = start.find_next_sibling()
            if start:
                for H in start.find_next_siblings():
                    if start is not None and start.name != 'p':
                        break
                    else:
                        Erwaegungen[0].append(H.get_text())
            break

        """""""Vorkalkulationen"""""""
        temp = start.find_next_sibling()
        num = Numbers[0]
        nextnum = Numbers[1]
        Test_next_line_numeric = temp.get_text()[0:len(nextnum)].replace('.', '').isnumeric()
        Test_next_prev_same = temp.get_text()[0:len(nextnum)] is not start.get_text()[0:len(num)]
        Test_line_to_cut = start.get_text()[0:len(num)].replace('.', '').isnumeric()
        to_save_cut = start.get_text()[len(num):]
        to_save = start.get_text()
        """"""""""""""""""""""""""""""

        if Test_next_line_numeric and Test_next_prev_same:
            if Test_line_to_cut:
                Erwaegungen[num].append(to_save_cut)
            else:
                Erwaegungen[num].append(to_save)
            Numbers.pop(0)
            start = start.find_next_sibling()
        else:
            Erwaegungen[num].append(to_save)
            start = start.find_next_sibling()
    return Erwaegungen


find_text(article)
