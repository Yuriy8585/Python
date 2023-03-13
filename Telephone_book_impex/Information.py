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
            if len(phone_number) != 11:
                print('Must be 11 digits.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Please put numbers.')
    info.append(phone_number)
    description = input('Discription: ')
    info.append(description)
    return info


def writing_csv(info):
    file = 'Telephonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')


def writing_txt(info):
    file = 'Telephonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Last_name: {info[0]}\n\nName: {info[1]}\n\nTelephone_number: {info[2]}\n\nDiscription: {info[3]}\n\n\n')