def getWordsCollection(option=1):
    collection = []
    if option == 1:
        with open('five_letter_words.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                collection.append(line)
    else:
        collection = [
            'causa',
            'apraz'
        ]

    return collection