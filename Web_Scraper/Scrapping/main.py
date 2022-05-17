import Scrapping.cms_fix
import json
Leitentscheide = ['147-II-186']

if __name__ == '__main__':
    for value in Leitentscheide:
        html = 'https://bger.li/'+value
        Erw = Scrapping.cms_fix.main(html)


