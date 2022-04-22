from bs4 import BeautifulSoup
import requests

source = requests.get("https://bger.li/147-III-218").text
soup = BeautifulSoup(source,'lxml')

article = soup.find('div', id='content')

def find_Erwaegung(article):
    for H in article.find_all('h1'):
        if H.get_text() == 'Erwägungen':
            return H

def get_text_Erw(H):
    abs = []
    for sibling in H.find_next_siblings():
        if sibling.name is None or sibling.name != 'p':
            break
        else:
            abs.append(sibling.get_text())
    return abs

print(get_text_Erw(find_Erwaegung(article)))

