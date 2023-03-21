import model
import view

def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранен')
            case 3:
                view.show_contacts(pb, 'phone book empty')

            case 4:
                model.add_contact(view.add_contact)
            case 5:
                if view.show_contacts(pb, 'phone book empty'):
                    index = view.input_index('Enter phone number')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменён')
            case 6:
                model.find_contact(view.input_search)
                search = view.input_search('Enter name or telephone')
                result = model.find_contact(search)
                view.show_contacts(result, 'No contact in the list')
            case 7:
                return

