# Содержит метод вывода информации из текстового файла в консоль.

def from_file(file):
    file = 'Telephone_book_impex/Telephonebook.csv'
    with open(file, 'r', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary