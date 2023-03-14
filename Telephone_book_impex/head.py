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
    #info = []
    flag = input('Press \'Y\' to create new write or any other symbol to exit:  ')
    while (flag.lower() == 'y'):
        path = 'Telephone_book_impex/Telephonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input('Press key to open file or any other symbol to exit: \n1: Save phonebook, \n2: Show all contacts, \n3: Find contact '
                         '\n4: Add contact, \n5: Edit contact, \n6: Delete contact, \n7: Exit \n:key-->')
        if choice_action == '4':
            record_info()
        if choice_action == '1':
                info = information()
                writing_csv(info)
                writing_txt(info)
        if choice_action == '2':
            view()
        if choice_action == '3':
            info = information()
            findcl(info)
        if choice_action == '5':
            info = information()
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


# Проверка существующего списка
path_to_r = 'Telephone_book_impex/Telephonebook.txt'
with open(path_to_r, 'r', encoding = 'UTF-8') as file:
    data = file.readlines()
print(data)