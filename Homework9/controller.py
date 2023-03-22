import phonebookclass


pb = phonebookclass.PhoneBook('phoneBook2.txt')


while True:
    print(pb.menu())
    choise = int(input('Choose menu: '))
    match choise:
        case 1:
            print(pb)
        case 2:
            name = input('Enter name: ')
            phone_number = input('Enter telephone number: ')
            valid = False
            while not valid:
                try:
                    phone_number = input('Enter VALID telephone number: ')
                    if len(phone_number) < 11:
                        print('Must be 11 or more digits.')
                    else:
                            phone_number = int(phone_number)
                            valid = True
                except:
                    print('Please put numbers.')
            email = input('Input email: ')
            pb.new_contact(name, phone_number, email)

        case 3:
            name = input('Input name: ')
            pb.search_by_name(name)
        case 4:
            print(pb)
            index = int(input('Enter index contact: '))
            name = input('Input name: ')
            phone_number = input('Enter telephone number: ')
            valid = False
            while not valid:
                try:
                    phone_number = input('Enter VALID telephone number: ')
                    if len(phone_number) < 11:
                        print('Must be 11 or more digits.')
                    else:
                            phone_number = int(phone_number)
                            valid = True
                except:
                    print('Please put numbers.')
            email = input('Input email: ')
            pb.change(index-1, name, phone_number, email)  # Индекс -1 !!!!
        case 5:
            print(pb)
            index = int(input('Input index contact: '))
            pb.delete(index-1)
        case 6:
            pb.save()
            
        case 7:
            break

