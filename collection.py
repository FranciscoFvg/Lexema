from unidecode import unidecode

collection = []
collectionAccent = []

def getWordsCollection(option='main'):
    global collection, collectionAccent
    if option == 'main':
        with open('five_letter_words.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                collectionAccent.append(line)
                collection.append(unidecode(line))
    elif option == 'tests':
        collection = [
            'causa',
            'apraz'
        ]


def getWordFromCollectionAccent(word):
    global collection, collectionAccent
    index = collection.index(word)
    return collectionAccent[index]