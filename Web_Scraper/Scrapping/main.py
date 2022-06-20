import cms_fix

Leitentscheide = ['136 II 5', '136 II 304', '136 II 436',
                  '136 II 551', '137 II 177', '137 II 242',
                  '137 II 246', '137 II 254', '137 II 266',
                  '137 II 284', '137 II 297', '137 II 305',
                  '137 II 313', '137 II 328', '137 II 338',
                  '137 II 345', '137 II 353', '137 II 366',
                  '137 II 371', '137 II 383', '146 III 142',
                  '146 III 157', '146 III 169', '146 III 177',
                  '146 III 185', '146 III 194', '146 III 203',
                  '146 III 217', '146 III 225', '146 III 237',
                  '146 III 247', '146 III 254', '143 III 3',
                  '143 III 10', '143 III 15', '143 III 21',
                  '143 III 28', '143 III 38', '143 III 42',
                  '143 III 46', '143 III 51', '143 III 55',
                  '143 III 65', '143 III 73', '141 V 127',
                  '141 V 139', '141 V 148', '141 V 155',
                  '141 V 162', '141 V 170', '141 V 175',
                  '141 V 186', '141 V 191', '141 V 197',
                  '141 V 206', '141 V 216'
                  ]


if __name__ == '__main__':
    for value in Leitentscheide:
        html = 'https://bger.li/' + value.replace(' ', '-')
        Erw = cms_fix.main(html)
