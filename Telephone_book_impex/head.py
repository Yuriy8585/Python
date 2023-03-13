# Предоставляет пользователю возможность выбрать продолжить работу или завершить, записывать данные или выводить на экран.

from os.path import exists
from createwrite import creating
from Information import writing_csv, writing_txt, information
from Record import from_file


def view():
    print(from_file('Telephone_book_impex/Telephonebook.txt'))

def record_info():
    info = information()
    writing_csv(info)
    writing_txt(info)


def choice():
    flag = input(
        'Press \'Y\' to open file or any other symbol to exit: ')
    while (flag.lower() == 'y'):
        path = 'Telephone_book_impex/Telephonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Press \'Y\' to create new write or any other symbol to exit:  ')
        if choice_action.lower() == 'y':
            record_info()
        else:
            view()
        flag = input(
            'Press any key to exit: ')
    print('Saved!')
path_to_r = 'Telephone_book_impex/Telephonebook.txt'
with open(path_to_r, 'r', encoding = 'UTF-8') as file:
    data = file.readlines()
print(data)