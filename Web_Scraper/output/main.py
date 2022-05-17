import Scrapping.cms_fix
import json


def write_out_json(Erw, html):
    with open('output/' + Scrapping.cms_fix.get_name(html) + '.json', 'w') as js:
        json.dump(Erw, js)
    js.close()


if __name__ == '__main__':
    html = 'https://bger.li/147-II-209'
    Erw = Scrapping.cms_fix.main(html)
    write_out_json(Erw, html)
