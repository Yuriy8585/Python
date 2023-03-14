# Предоставляет пользователю возможность выбрать продолжить работу или завершить, записывать данные или выводить на экран.

from os.path import exists
from createwrite import creating
from Information import writing_csv, writing_txt, information, findcl, add_client
from Record import from_file


def view():
    print(from_file('Telephone_book_impex/Telephonebook.txt'))

def record_info(): # Берем ф-ции из информации
    info = information()
    writing_csv(info)
    writing_txt(info)


def choice():
    flag = input('Press \'Y\' to create new write or any other symbol to exit:  ')
    while (flag.lower() == 'y'):
        path = 'Telephone_book_impex/Telephonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input('Press key to open file or any other symbol to exit: \n1: Сохранить телефонную книгу, \n2: Показать все контакты, \n3: Найти контакт '
                        '\n4: Добавить контакт, \n5: Изменить контакт,  \n6: Удалить контакт, \n7: Выход \n:_____')
        if choice_action == '4':
            record_info()
        if choice_action == '1':
                info = information()
                writing_csv(info)
                writing_txt(info)
        if choice_action == '2':
            view()
        if choice_action == '3':
            findcl(info)
        if choice_action == '5':
            new_cntc = findcl(info)
            add_client(info, new_cntc)
        if choice_action == '6':
            record_info()
        if choice_action == '7':
            break
        else:
            print('Wrong choice')
            view()
        flag = input(
                'Press any key to exit: ')
    print('Saved!')

"""
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
"""
# Проверка существующего списка
path_to_r = 'Telephone_book_impex/Telephonebook.txt'
with open(path_to_r, 'r', encoding = 'UTF-8') as file:
    data = file.readlines()
print(data)