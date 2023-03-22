# Позволяет ввести данные для дальнейшого сохранения в телефонном справочнике. 
# В данном модюле присутствует проверка на количество символов в номере телефона, и проверка на число. 
# Все четыре категории данных, а именно фамилия, имя, номер телефона и описание, сохраняются в списке `info`.

file = 'Telephone_book_impex/Telephonebook.csv'
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
    
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Last_name: {info[0]}\nName: {info[1]}\nTelephone_number: {info[2]}\nDiscription: {info[3]}\n\n')


def writing_txt(info):
    
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Last_name: {info[0]}\nName: {info[1]}\nTelephone_number: {info[2]}\nDiscription: {info[3]}\n\n')


def add_client(info, new_last_name):
    if len(new_last_name):
        last_name = input('Last Name : ')
        info(last_name)
        first_name = input('Your name : ')
        info(first_name)
        phone_cntc = int(input('Enter phone number : '))
        info(phone_cntc)
        comment_cntc = input('Discription : ')
        info(comment_cntc)
        cntc_list = [phone_cntc, comment_cntc]
    writing_csv (info)
    writing_txt(info)
    return {'Last_name': info[0], 'Name': info[1], 'Telephone_number': info[2], 'Discription': info[3], 'Client_list': cntc_list}       

