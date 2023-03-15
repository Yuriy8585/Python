# Позволяет ввести данные для дальнейшого сохранения в телефонном справочнике. 
# В данном модюле присутствует проверка на количество символов в номере телефона, и проверка на число. 
# Все четыре категории данных, а именно фамилия, имя, номер телефона и описание, сохраняются в списке `info`.


def information():
    info = []
    last_name = input('Last Name : ')
    info.append(last_name)
    first_name = input('Your name : ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Telefone number : ')
            if len(phone_number) < 11:
                print('Must be 11 or more digits.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Please put numbers.')
    info.append(phone_number)
    description = input('Discription: ').lower()
    info.append(description)
    return info


def writing_csv(info):
    file = 'Telephone_book_impex/Telephonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Last_name: {info[0]}\n\nName: {info[1]}\n\nTelephone_number: {info[2]}\n\nDiscription: {info[3]}\n\n\n')


def writing_txt(info):
    file = 'Telephone_book_impex/Telephonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Last_name: {info[0]}\n\nName: {info[1]}\n\nTelephone_number: {info[2]}\n\nDiscription: {info[3]}\n\n\n')

def findcl(info):
    file = 'Telephone_book_impex/Telephonebook.txt'
    with open(file, 'r', encoding = 'UTF-8') as data:
        name_cntc = input('Input Last Name ')
        data = data.readlines()
        if name_cntc in info:
            print(f'Last_name: {info[0]}\n\nName: {info[1]}\n\nTelephone_number: {info[2]}\n\nDiscription: {info[3]}\n\n\n')
        else:
            print(f'Not Found {name_cntc}')

def add_client(info, new_last_name = [0]):
    if len(new_last_name) != 0:
        last_name = input('Last Name : ')
        info.append(last_name)
        first_name = input('Your name : ')
        info.append(first_name)
        phone_cntc = int(input('Enter phone number : '))
        info.append(phone_cntc)
        comment_cntc = input('Discription : ')
        info.append(comment_cntc)
        cntc_list = [phone_cntc, comment_cntc]
    else:
        last_name, first_name, cntc_list = tuple(new_last_name)
    # info[name_cntc] = info.setdefault(name_cntc, cntc_list)
    info.setdefault(last_name, first_name, cntc_list)
    print(f'{new_last_name}, {info[new_last_name]}')
    return info        

