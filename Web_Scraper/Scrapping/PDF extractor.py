# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('example.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#page number
number_of_pages = pdfReader.getNumPages()
array = []
Erw = []
start = False
#for loop to extract from multiple pages
for page_number in range(number_of_pages):
    page = pdfReader.getPage(page_number)
    ray_to_control = page.extractText().split(u'Erwägungen')
    if (len(ray_to_control) > 1) or start:
        start = True
        array.append(page.extractText())


# printing number of pages in pdf file


# creating a page object




# extracting text from page

my_text = array[0].split(u'Aus den Erwägungen:')

array[0] = my_text[1]

for string in array:
    temp = string.split(u'\n')
    for x in temp:
        Erw.append(x)
absatz = ''
cnt = -1
for string in Erw:
    cnt = cnt + 1
    if cnt > len(Erw):
        cnt = len(Erw)-1
    if string.replace('.','').replace(' ','').isnumeric():
        ISNUMERIC = True
    else:
        ISNUMERIC = False

    if ISNUMERIC:
        continue
    elif not ISNUMERIC and !Erw[cnt + 1].replace('.','').replace(' ','').isnumeric():
        absatz = absatz + " " + string



# closing the pdf file object
pdfFileObj.close()

"""
strValue = array
ch = '\nErwägungen\n'
strValue = strValue.split(ch,1) [1]
print(strValue)
"""