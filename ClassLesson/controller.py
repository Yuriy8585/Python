import phonebookclass

pb = phonebookclass.PhoneBook('phonebook.txt')

"""
print(pb)
pb.new_contact('Kirill', '+7123456789', 'kirill@mail.ru')
#print(pb.phone_list[1])
print(pb)
pb.save()
print(pb.search('0'))
"""

while True:
    print(pb.menu())
    choise = int(input('Выберите пункт меню: '))
    match choise:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone_number = input('Введите номер телефона: ')
            email = input('Введите email: ')
            pb.new_contact(name, phone_number, email)
        case 3:
            name = input('Введите имя: ')
            pb.search_by_name(name)
        case 4:
            print(pb)
            index = int(input('Введите индекс контакта: '))
            name = input('Введите имя: ')
            phone_number = input('Введите номер телефона: ')
            email = input('Введите email: ')
            pb.change(index-1, name, phone_number, email)  # Индекс -1 !!!!
        case 5:
            print(pb)
            index = int(input('Введите индекс контакта: '))
            pb.delete(index-1)
        case 6:
            pb.save()
        case 7:
            break