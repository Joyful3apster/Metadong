import collections
import requests
from bs4 import BeautifulSoup
import Database_Con
import unidecode


def format_html(html):
    source = requests.get(html).text
    soup = BeautifulSoup(source, 'lxml')
    div = soup.find('div', id='content')
    return div


def get_name(html):
    string = html.split('/')
    name = str(string[3])
    return name


def find_start(div):
    """@:return h1 tag mit Inhalt Erwägung im Leitentscheid als Ankerpunkt"""
    for H in div.find_all('h1'):
        if H.get_text() == 'Erwägungen':
            return H


def find_number(div):
    """Unter gegeben html "Ankerpunkt" gibt es nummerische Absätze
    mit tag <strong>.
    @:parameter html Ankerpunkt zum durch iterieren
    @:return Diese Nummer werden als Liste zurückgegeben """

    number = []
    for H in div.find_all('strong'):
        if H is not None and H.name != 'p':
            if H.get_text().replace('.', '').isnumeric():
                number.append(H.get_text())
    return number


def delete_span_tag(H):

    for span_Tag in H.findAll('span', class_="pagebreak"):
        span_Tag.replace_with('')
    return H


def dict_gen(div):
    """Erstellt ein @:rtype dict (default list)
    @:return: Erstellt dict mit allen Absätzen (values) zum passender Nummer (keys)
    @:parameter:html: Html Datei"""

    Numbers = find_number(div)
    start = delete_span_tag(find_start(div))

    """Dict initialisieren"""
    Erwaegungen = collections.defaultdict(list)

    """Element 'Aus den Erwägungen:' überspringen"""
    start = delete_span_tag(start.find_next_sibling().find_next_sibling())

    """Algorithmus"""
    while True:

        """Handling wenn Numbers genau ein Element noch hat"""
        if len(Numbers) == 1:
            last_num = Numbers[0]
            first = start.get_text().encode('utf-8').decode()[len(last_num):]
            first = unidecode.unidecode(first)
            Erwaegungen[last_num].append(first)
            start = start.find_next_sibling()
            if start:
                for H in start.find_next_siblings():
                    if H is not None and H.name != 'p':
                        Numbers.pop(0)
                        break
                    else:
                        word = H.get_text().encode('utf-8').decode()
                        word = unidecode.unidecode(word)
                        Erwaegungen[last_num].append(word)
            Numbers.pop(0)
            break

        """""""Vorkalkulationen"""""""
        temp = delete_span_tag(start.find_next_sibling())
        num = Numbers[0]
        nextnum = Numbers[1]
        Test_next_line_numeric = temp.get_text()[0:len(nextnum)].replace('.', '').isnumeric()
        Test_next_prev_same = temp.get_text()[0:len(nextnum)] is not start.get_text()[0:len(num)]
        Test_line_to_cut = start.get_text()[0:len(num)].replace('.', '').isnumeric()
        get_encoding_cut = start.get_text().encode('utf-8').decode()[len(num):]
        to_save_cut = unidecode.unidecode(get_encoding_cut)
        get_encoding = start.get_text().encode('utf-8').decode()
        to_save = unidecode.unidecode(get_encoding)
        """"""""""""""""""""""""""""""

        if Test_next_line_numeric and Test_next_prev_same:
            if Test_line_to_cut:
                Erwaegungen[num].append(to_save_cut)
            else:
                Erwaegungen[num].append(to_save)
            Numbers.pop(0)
            start = delete_span_tag(start.find_next_sibling())
        else:
            if Test_line_to_cut:
                Erwaegungen[num].append(to_save_cut)
            else:
                Erwaegungen[num].append(to_save)
            start = delete_span_tag(start.find_next_sibling())

    return Erwaegungen


def main(html):
    div = format_html(html)
    name = get_name(html)
    Erw = dict_gen(div)
    Database_Con.add_one(Erw, name)
