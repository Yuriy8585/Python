# Модуль создает файл `.csv` и записывает в него данные для таблицы.

def creating():
    file = 'Telephone_book_impex/Telephonebook.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Secondname;Name;Telephone Number;Dicription\n')