import cms_fix

Leitentscheide = ['124-III-201', '']

if __name__ == '__main__':
    for value in Leitentscheide:
        html = 'https://bger.li/'+value
        Erw = cms_fix.main(html)


