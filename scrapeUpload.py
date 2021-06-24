

import bs4, requests, docx, os


def scrapeWord(word):  # function definition for finding word
    try:
        base_url = 'https://www.dictionary.com/browse/' + word
        opened_url = requests.get(base_url).text
        parsed_url = bs4.BeautifulSoup(opened_url, 'lxml')
        definition = parsed_url.find('span', class_='one-click-content css-nnyc96 e1q3nk1v1').text
        return definition  # returns a string that is the meaning
    except AttributeError:
        error = 'No meaning found'
        return error  # returns error string


wordList = []
meaningList = []
count = 0

while True:  # infinite loop to add word and meanings to the list above
    print('Find meaning of:')
    word = input()
    if word != '':
        print('Your word: ' + word)
        print(scrapeWord(word))
        wordList.append(word)
        meaningList.append(scrapeWord(word).lower())
        count += 1
    else:
        break

d = docx.Document()  # declaration of 'd' document variable

for i in range(count):
    d.add_paragraph(wordList[i] + " - " + meaningList[i])

filename = input('Save as: ')

d.save('C:/Users/' + os.getenv('username') + '/Desktop/' + filename + '.docx')


