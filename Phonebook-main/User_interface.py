def get_info ():
    info = []
    last_name = input('Enter Lastname: ')
    info.append(last_name)
    first_name = input('Enter name: ')
    info.append(first_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Enter telefone number: ')
            if len(phone_number) != 11:
                print('Must be 11 numbers in telefone number.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Must be numbers in telefone number!.')
    info.append(phone_number)
    description = input('Discription: ')
    info.append(description)
    return info