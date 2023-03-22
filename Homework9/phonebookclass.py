class Contact:
    def __init__(self, name: str, phone_number: str, email: str):
        self.path = 'phoneBook2.txt'
        self.name = name
        self.phone_number = phone_number
        self.email = email
    def __str__(self):
        return f"{self.name:<20} has phone number {self.phone_number:<20} and email {self.email:<20}"
    
    def to_str(self):
        return f"{self.name:<20} has phone number {self.phone_number:<20} and email {self.email:<20}"
    

class PhoneBook:
    def __init__(self, path: str):
        self.path = path
        self.phone_list = []
        self.open()
    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as f:
            data = f.readlines()
        for contact in data:
            new_contact = contact.strip().split(':')
            self.phone_list.append(Contact(*new_contact))
    def save(self):
        data = '\n'.join([contact.to_str() for contact in self.phone_list])
        with open(self.path, 'w', encoding='UTF-8') as f:
            f.write(data)

    def menu(self):
        return '''Главное меню
        1. Вывести всех контактов
        2. Создать новый контакт
        3. Найти контакт по имени
        4. Изменить контакт
        5. Удалить контакт
        6. Сохранить
        7. Выход
        '''


    def new_contact(self, name: str, phone_number: str|int, email: str):
        self.phone_list.append(Contact(name, phone_number, email))

    def search_by_name(self, find: str):
        result = []
        for contact in self.phone_list:
            if find in contact.to_str():
                result.append(f'{contact}')
        return '\n'.join(result)

    def change(self, index: int, name: str, phone_number: str, email: str):
        name = name if name != '' else self.phone_list[index].name
        phone_number = phone_number if phone_number != '' else self.phone_list[index].phone_number
        email = email if email != '' else self.phone_list[index].email
        self.phone_list[index] = Contact(name, phone_number, email)


    def delete(self, index: int):
        self.phone_list.pop(index)
        self.save()

    def __str__(self):
        result = ''
        i= 0
        for contact in self.phone_list:
            i+=1
            result += f'{i}{contact}\n'
        return result[:-2]
    
