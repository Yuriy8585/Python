# Предоставляет пользователю возможность выбрать продолжить работу или завершить, записывать данные или выводить на экран.

from os.path import exists
from createwrite import creating
from Information import writing_csv, writing_txt, information, findcl, add_client
from Record import from_file


def choice():
    info = []
    flag = input('Press \'Y\' to create new write or any other symbol to exit:  ')
    while (flag.lower() == 'y'):
        path = 'Telephone_book_impex/Telephonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input('Press key to open file or any other symbol to exit: \n1: Save phonebook, \n2: Show all contacts, \n3: Find contact '
                         '\n4: Add contact, \n5: Edit contact, \n6: Delete contact, \n7: Exit \n:key-->')
        
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
            record_info()
        if choice_action == '4':
            view()
            record_info()
            view()    
        if choice_action == '6':
            remove_string_from_list()
            view()
        if choice_action == '7':
            break
        else:
            print('DONE')
            
        flag = input(
                'Press any key to exit: ')
    print('Saved!')

def view():
    print(from_file('Telephone_book_impex/Telephonebook.txt'))



def record_info(): # Берем ф-ции из информации
    info = information()
    writing_csv(info)
    writing_txt(info)

def delete_info():
    with open('Telephone_book_impex/Telephonebook.csv', "r") as f:
        lines = f.readlines()
    with open('Telephone_book_impex/Telephonebook.csv', "w") as f:
        for line in lines:
            if line.strip("\n") != input("Lastname_to_delete: "):
                f.write(line)
            elif print("RESULT"):
                view()
                break
                
# программа которая удаляет строку из списка

def remove_string_from_list(info, lines):
    with open('Telephone_book_impex/Telephonebook.csv', "w") as f:
        for lines in lines:
            lines = input('Enter Last name to remove: ')
            info.remove(lines)
            return info
    print(remove_string_from_list(['a', 'b', 'c'], 'a'))
    print(remove_string_from_list(['a', 'b', 'c'], 'd'))
    print(remove_string_from_list(['a', 'b', 'c'], 'c'))

# Проверка существующего списка
path_to_r = 'Telephone_book_impex/Telephonebook.txt'
with open(path_to_r, 'r', encoding = 'UTF-8') as file:
    data = file.readlines()
print(data)