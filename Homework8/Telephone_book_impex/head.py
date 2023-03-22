# Предоставляет пользователю возможность выбрать продолжить работу или завершить, записывать данные или выводить на экран.
from os.path import exists
from createwrite import creating
from Information import writing_csv, writing_txt, information, add_client
from Record import from_file

phone_book = []

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
            find_contact(input_search)
            search = input_search('Enter name or telephone')
            info = find_contact(search)
            #findcl(info)
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
    print(from_file('Telephonebook.txt'))

def input_index(message: str):
    return int(input(message))

def input_search(message):
    return input(message)

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

def findcl(info):
    
    with open(file, 'r', encoding = 'UTF-8') as data:
        name_cntc = input('Input Last Name ')
        data = data.readlines()
        if name_cntc in info:
            print(f'Last_name: {info[0]}\n\nName: {info[1]}\n\nTelephone_number: {info[2]}\n\nDiscription: {info[3]}\n\n\n')
        else:
            print(f'Not Found {name_cntc}')

def find_contact(search: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for field in contact.values():
            if search.lower() in field.lower():
                result.append(contact)
    
            else:
                print(f'Not Found {search}')
    return result            
# программа которая удаляет строку из списка

def remove_string_from_list(info, lines):
    with open('Telephone_book_impex/Telephonebook.csv', "w") as f:
        for lines in lines:
            lines = input('Enter Last name to remove: ')
            info.remove(lines)
            return info
    print(remove_string_from_list(['a', 'b', 'c'], 'a'))


# Проверка существующего списка
path_to_r = 'Telephone_book_impex/Telephonebook.txt'
with open(path_to_r, 'r', encoding = 'UTF-8') as file:
    data = file.readlines()
print(data)