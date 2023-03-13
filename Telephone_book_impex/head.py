# Предоставляет пользователю возможность выбрать продолжить работу или завершить, записывать данные или выводить на экран.

from os.path import exists
from createwrite import creating
from Information import writing_csv, writing_txt, information
from Record import from_file


def view():
    print(from_file('Telephonebook.txt'))


def record_info():
    info = information()
    writing_csv(info)
    writing_txt(info)


def choice():
    flag = input(
        'Press \'Y\' to continue or any other symbol to exit: ')
    while (flag.lower() == 'Y'):
        path = 'Telephonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Press \'Y\' to continue or any other symbol to exit:  ')
        if choice_action.lower() == 'Y':
            record_info()
        else:
            view()
        flag = input(
            'Press \'Y\' to continue or any other symbol to exit: ')
    print('Saved!')
